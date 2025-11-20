const express = require('express');
const fs = require('fs');
const path = require('path');
const cors = require('cors');

const app = express();
app.use(express.json());
app.use(cors());
app.use(express.static(__dirname));

const DATA_DIR = __dirname;

// Get all categories
app.get('/api/categories', (req, res) => {
    const filePath = path.join(DATA_DIR, 'categories.json');
    if (fs.existsSync(filePath)) {
        res.json(JSON.parse(fs.readFileSync(filePath, 'utf8')));
    } else {
        res.json([]);
    }
});

// Get stories by category
app.get('/api/stories/:category', (req, res) => {
    const { category } = req.params;
    const filePath = path.join(DATA_DIR, `${category}.json`);

    if (fs.existsSync(filePath)) {
        res.json(JSON.parse(fs.readFileSync(filePath, 'utf8')));
    } else {
        res.json([]);
    }
});

// Add/Update story
app.post('/api/stories/:category', (req, res) => {
    try {
        const { category } = req.params;
        const story = req.body;
        const filePath = path.join(DATA_DIR, `${category}.json`);

        let stories = [];
        if (fs.existsSync(filePath)) {
            stories = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        }

        const index = stories.findIndex(s => s.id === story.id);
        if (index > -1) {
            stories[index] = story;
        } else {
            stories.push(story);
        }

        fs.writeFileSync(filePath, JSON.stringify(stories, null, 2));
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Delete story
app.delete('/api/stories/:category/:id', (req, res) => {
    try {
        const { category, id } = req.params;
        const filePath = path.join(DATA_DIR, `${category}.json`);

        if (!fs.existsSync(filePath)) {
            return res.status(404).json({ error: 'Category not found' });
        }

        let stories = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        stories = stories.filter(s => s.id !== id);

        fs.writeFileSync(filePath, JSON.stringify(stories, null, 2));
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Add category
app.post('/api/categories', (req, res) => {
    try {
        const newCategory = req.body;
        const filePath = path.join(DATA_DIR, 'categories.json');
        let categories = [];

        if (fs.existsSync(filePath)) {
            categories = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        }

        const index = categories.findIndex(c => c.id === newCategory.id);
        if (index > -1) {
            categories[index] = newCategory;
        } else {
            categories.push(newCategory);
            // Create empty data file
            const dataPath = path.join(DATA_DIR, `${newCategory.id}.json`);
            if (!fs.existsSync(dataPath)) {
                fs.writeFileSync(dataPath, '[]');
            }
        }

        fs.writeFileSync(filePath, JSON.stringify(categories, null, 2));
        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Delete category
app.delete('/api/categories/:id', (req, res) => {
    try {
        const { id } = req.params;
        const filePath = path.join(DATA_DIR, 'categories.json');

        if (!fs.existsSync(filePath)) {
            return res.status(404).json({ error: 'Categories file not found' });
        }

        let categories = JSON.parse(fs.readFileSync(filePath, 'utf8'));
        categories = categories.filter(c => c.id !== id);
        fs.writeFileSync(filePath, JSON.stringify(categories, null, 2));

        // Optionally delete data file
        const dataPath = path.join(DATA_DIR, `${id}.json`);
        if (fs.existsSync(dataPath)) {
            fs.unlinkSync(dataPath);
        }

        res.json({ success: true });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

// Push to GitHub
app.post('/api/push', (req, res) => {
    const { exec } = require('child_process');
    exec('git add . && git commit -m "Updated stories via Admin Panel" && git push', (error, stdout, stderr) => {
        if (error) {
            console.error(`Git error: ${error}`);
            return res.status(500).json({ success: false, message: stderr });
        }
        res.json({ success: true, message: 'Changes pushed to GitHub!' });
    });
});

const PORT = 8080;
app.listen(PORT, () => {
    console.log(`✅ Server running at http://localhost:${PORT}`);
    console.log(`📝 Admin Panel: http://localhost:${PORT}/admin.html`);
});

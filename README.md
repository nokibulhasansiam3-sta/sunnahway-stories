# Sunnahway Stories

এই repository তে Sunnahway app এর সব গল্প (stories) রাখা আছে JSON format এ।

## 📁 File Structure

```
sunnahway-stories/
├── categories.json          # Story categories list
├── nobider_jibon_theke.json # নবীদের জীবন থেকে
├── sahabider_jibon_theke.json # সাহাবীদের জীবন থেকে
├── itihasher_golpo.json     # ইতিহাসের গল্প
└── ... (more story files)
```

## 🔗 Raw URL

App থেকে এই URL দিয়ে stories load হয়:

```
https://raw.githubusercontent.com/YOUR_USERNAME/sunnahway-stories/main/
```

## ➕ নতুন গল্প যোগ করার নিয়ম

### 1. নতুন category যোগ করতে:

`categories.json` এ নতুন entry add করো:

```json
{
  "id": "new_category_id",
  "title": "নতুন ক্যাটাগরি নাম"
}
```

### 2. নতুন story file বানাও:

File name: `new_category_id.json`

Format:
```json
[
  {
    "id": "story-unique-id",
    "categoryId": "new_category_id",
    "title": "গল্পের শিরোনাম",
    "paragraphs": [
      "প্রথম প্যারাগ্রাফ...",
      "দ্বিতীয় প্যারাগ্রাফ..."
    ],
    "moral": "শিক্ষা/নৈতিকতা",
    "source": "সূত্র"
  }
]
```

### 3. GitHub এ push করো:

```bash
git add .
git commit -m "Added new stories"
git push
```

✅ সব user এর কাছে automatically update পৌঁছে যাবে!

## 📝 Important Notes

- **Arabic text**: Quranic ayat এর জন্য Arabic text রাখা যাবে
- **Bengali text**: সব story content Bengali তে লিখতে হবে
- **No mixed text**: Bengali paragraph এ Arabic word mix করা যাবে না
- **File encoding**: UTF-8 encoding use করতে হবে

## 🚀 App Integration

App automatically এই repository থেকে stories load করে এবং local এ cache করে রাখে। Internet connection প্রথমবার লাগবে, পরে offline এ কাজ করবে।

---

Made with ❤️ for Sunnahway App

# 🚀 GitHub Setup Instructions

## Step 1: GitHub এ Repository বানাও

1. **GitHub.com এ যাও**: https://github.com/new
2. **Repository name**: `sunnahway-stories`
3. **Description**: "Story content for Sunnahway Islamic App"
4. **Public** select করো (free hosting এর জন্য)
5. **"Create repository"** button এ click করো

## Step 2: Local Repository Push করো

Terminal এ এই commands run করো:

```bash
cd /Users/nasimulhasan/Desktop/sunnahway-stories

# তোমার GitHub username দিয়ে replace করো
git remote add origin https://github.com/YOUR_USERNAME/sunnahway-stories.git

# Push করো
git branch -M main
git push -u origin main
```

## Step 3: App Code এ URL Update করো

File: `lib/features/stories/data/story_repository.dart`

Line 41-42 এ তোমার GitHub username দিয়ে replace করো:

```dart
static const String? githubBaseUrl = 
    'https://raw.githubusercontent.com/YOUR_ACTUAL_USERNAME/sunnahway-stories/main/';
```

**Example:** যদি তোমার username হয় `nasimul123`, তাহলে:

```dart
static const String? githubBaseUrl = 
    'https://raw.githubusercontent.com/nasimul123/sunnahway-stories/main/';
```

## Step 4: Test করো

1. App run করো
2. Stories section এ যাও
3. প্রথমবার internet লাগবে (GitHub থেকে download হবে)
4. পরে offline এ কাজ করবে

## ✅ Done!

এখন থেকে:
- App size অনেক কমে যাবে (stories assets এ নেই)
- GitHub এ নতুন story add করলে সব user এর কাছে পৌঁছাবে
- Completely FREE hosting!

## 📝 নতুন Story যোগ করার জন্য:

1. `sunnahway-stories` folder এ নতুন story add করো
2. Git commit করো:
   ```bash
   cd /Users/nasimulhasan/Desktop/sunnahway-stories
   git add .
   git commit -m "Added new stories"
   git push
   ```
3. ✅ Done! সব user এর কাছে automatic update যাবে

---

## 🔧 Troubleshooting

**যদি stories load না হয়:**
- Internet connection check করো
- GitHub URL ঠিক আছে কিনা check করো
- GitHub repository public আছে কিনা check করো

**Local fallback:**
- GitHub fail করলে app automatically local assets থেকে load করবে
- So app কখনো break হবে না!

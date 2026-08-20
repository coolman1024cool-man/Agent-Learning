# Firebase 網頁開發與部署實戰紀錄

這份文件記錄了我們如何從零開始，利用 Firebase Hosting 架設「敏實科技大學 USR 計畫中心」專屬網頁的完整工作流程，方便未來隨時複習。

## 階段一：準備專案檔案
1. **建立專案資料夾**：
   在電腦中建立一個專屬資料夾（例如 `usr_website`）。
2. **準備素材資源**：
   將網頁需要的圖片（敏實科大 Logo、USR 圖章）準備好，放進專案資料夾中。我們建立了一個 `public` 子資料夾來專門存放對外公開的檔案。
3. **撰寫網頁原始碼 (HTML)**：
   使用 HTML 語言與 Bootstrap 5 框架，將海報上的「六大亮點成果」與「合作夥伴」轉化為網頁排版，並儲存為 `public/index.html`。

## 階段二：設定 Firebase 專案連線
為了讓電腦知道這個網頁要上傳到哪一個 Firebase 空間，我們在專案資料夾的根目錄建立了兩個設定檔：

1. **`.firebaserc`**：告訴系統要綁定哪一個專案 ID（例如：`my-first-app-1150820`）。
   ```json
   {
     "projects": {
       "default": "my-first-app-1150820"
     }
   }
   ```

2. **`firebase.json`**：告訴系統在部署時，要把哪個資料夾的內容上傳（在這裡我們指定了剛剛整理好的 `public` 資料夾）。
   ```json
   {
     "hosting": {
       "public": "public",
       "ignore": [
         "firebase.json",
         "**/.*",
         "**/node_modules/**"
       ]
     }
   }
   ```

## 階段三：一鍵部署上雲端
一切準備就緒後，在終端機（或透過 AntiGravity 系統）執行以下這行神聖的指令：

```bash
firebase deploy --only hosting
```

系統就會自動將 `public` 資料夾裡的所有圖片跟 HTML 網頁打包，上傳到 Google 的伺服器，並立刻產生一組專屬的網址：`https://my-first-app-1150820.web.app`。

---
**💡 架構師小叮嚀：**
未來如果網頁有任何修改（例如新增了 YouTube 影片），只要將 `index.html` 存檔後，再次執行 `firebase deploy --only hosting`，全世界的使用者就能立刻看到更新後的網頁囉！

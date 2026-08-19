from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

slides_data = [
    {
        "title": "Google AntiGravity 2.0 實測與 AI Agent 懶人包教學",
        "content": "專案總覽與核心概念\n\n• 核心概念：\n  - 將 AI Agent 的操作作業系統化 (OS-level)。\n  - 透過友善的圖形化介面 (GUI) 徹底簡化過去複雜的工作流程。\n  - 打造能在地端與雲端之間無縫協作的高效生產力環境。\n\n• 教學目標：\n  - 展示從零開始的安裝與基本操作。\n  - 實測多項外部工具的串接與整合能力。"
    },
    {
        "title": "強大的生態系連線能力",
        "content": "核心功能與外部整合\n\n• GitHub：直接管理 Repo、發布 PR 與程式碼版本控制。\n• NotebookLM：讀取雲端筆記大腦，將研究資料直接引入開發環境。\n• Firebase：自動化建置資料庫、部署規則與 Hosting。\n• Obsidian：與地端的個人知識庫 (MCPVault) 深度結合。\n\n亮點：無需反覆切換視窗，所有工具皆在同一個圖形化介面中由 Agent 代為操控。"
    },
    {
        "title": "為什麼我們需要懶人包 (Lazy Packs)？",
        "content": "「懶人包」的戰略意義\n\n• 快速複製最佳實踐：將複雜的設定檔與 Prompt 打包，一鍵載入。\n• 自動化建置專案：省去手動初始化環境的繁瑣步驟，實現開箱即用。\n• 進階任務生成：例如自動生成特定的資訊圖表、符合格式的報表等。\n• 降低學習門檻：讓非技術背景的使用者也能輕鬆駕馭強大的 AI Agent 能力。"
    },
    {
        "title": "真實測試的反饋與橫向對比",
        "content": "實測評價與競品比較\n\n• 實測發現的小瑕疵：\n  - 在處理「自動授權」流程時偶爾會卡頓。\n  - 部分終端機指令的執行邏輯仍有邊角問題 (Edge cases) 需要克服。\n• 與競品的橫向比較：\n  - 對比了 Claude Code 與 Codex 等知名對手。\n  - AntiGravity 2.0 在「圖形化體驗」與「系統級整合」上具備獨特優勢。\n• 階段性結論：整體展現強大潛力，為新一代 AI Agent 奠定基礎。"
    },
    {
        "title": "AI 代理人的未來發展趨勢",
        "content": "總結與未來展望\n\n• 作業系統化趨勢確立：AntiGravity 2.0 證明了 AI Agent 不再只是單一腳本，而是能接管系統流程的中樞。\n• 社群生態系為王：「懶人包」機制將能有效催生出龐大的社群共享生態，未來擴充性極佳。\n• 全民開發者時代：無論是專業工程師還是普通使用者，都能透過這套工具大幅釋放生產力。"
    }
]

for slide_data in slides_data:
    slide_layout = prs.slide_layouts[1] # Title and Content
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = slide_data["title"]
    content.text = slide_data["content"]
    
    # Adjust fonts to ensure CJK characters display nicely
    for paragraph in content.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.name = 'Microsoft JhengHei'
            
    for paragraph in title.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.name = 'Microsoft JhengHei'

prs.save("AntiGravity_Presentation.pptx")
print("Successfully generated AntiGravity_Presentation.pptx")

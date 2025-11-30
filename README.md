# 📘 Project Overview — AI Learning Coach (仮)

## 🎯 Purpose（目的）
本・紙／PC での学習・開発セッションを記録し、  
AI がセッションごと & 朝/夜に振り返り・計画・理解補助を行い、  
Obsidianと連携してツェッテルカステン形式のノートを自動生成する “学習コーチ兼 Knowledge Assistant” を作る。

- PC起動時に自動でAIが起動する
- 日々の計画（Today’s Goals）は AI が自動提案  
- セッション単位で「自分で短く説明」→ AI が要約/質問（理解度確認、内容確認）/次やること/ノート化  
- Obsidian（ツェッテルカステン）と自動連携  
- 長期・中期の目標は AI と定期的に策定し、日次は AI が切り出す
- 朝に日々の計画を提案して、夜にやったことをまとめて復習などを促す


# 🧭 Scope（範囲）

## ✔ このプロジェクトで実装すること（Phase1）
- 朝：Today’s Goals を AI がバックログから自動生成
- セッション（PC / BOOK）  
  PC学習：開始→終了説明→AIが要約/質問/次やること/ノート化  
  本・紙：書籍情報→終了後の説明→AI整理  
- 夜：Daily Summary（1日の総括＋明日のおすすめ）
- Obsidian連携（Zettelkasten形式のMDノート生成）

## ❌ このフェーズではやらないこと
- スマホ監視の自動化  
- ブラウザ強制ブロック  
- アニメキャラUI  
- Rust/Go製の常駐ロガー（後で追加）


# 🏗️ System Architecture（アーキテクチャ）

## 🌐 技術スタック（案）
- Frontend：Next.js（React, TypeScript）
- Backend：FastAPI（Python）
- AI：Azure OpenAI（API）
- DB：PostgreSQL
- Infra：Terraform + Azure Container Apps
- Container：Docker / docker-compose
- Knowledge：Obsidian（Markdown出力）

## 🏛️ Azure構成
- Azure Container Apps Environment（VNet統合）
  - ACA Frontend（Next.js）
  - ACA Backend（FastAPI）
- Azure Database for PostgreSQL
- Azure OpenAI
- Log Analytics Workspace

将来的に：
- Private Endpoint（DB / OpenAI）
- Application Insights


# 🗂️ Repository Structure（モノレポ）
現時点での構想
your-project-root/
├─ frontend/              # Next.js
│  ├─ src/
│  ├─ public/
│  ├─ Dockerfile
│  └─ package.json
│
├─ backend/               # FastAPI + LangChain/LangGraph
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ api/
│  │  ├─ core/
│  │  ├─ models/
│  │  ├─ services/
│  │  └─ llm/
│  ├─ tests/
│  ├─ Dockerfile
│  └─ pyproject.toml
│
├─ packages/              # 将来ライブラリ化するドメイン層
│  └─ study_core/
│     ├─ goals.py
│     ├─ sessions.py
│     └─ notes.py
│
├─ infra/
│  ├─ terraform/
│  │  ├─ main.tf
│  │  ├─ modules/
│  │  │  ├─ network/
│  │  │  ├─ container_apps/
│  │  │  └─ database/
│  │  └─ envs/
│  │     ├─ dev/
│  │     └─ prod/
│  └─ README.md
│
├─ scripts/
│  ├─ obsidian_export.py
│  └─ dev_tools/
│
├─ docker-compose.yml
├─ .env.example
├─ README.md
└─ docs/
   ├─ architecture.md
   └─ roadmap.md

## 💡 この構成の理由
- frontend / backend / infra が明確に分離され、学習効率が高い
- packages/study_core が「将来ライブラリ化の席」として機能
- docker-compose で開発環境が一発起動
- Azure Container Apps のデプロイと相性が良い
- 将来 Rust/Go ロガーを追加しやすい


# ⚙️ Core Features in Phase1（MVP仕様）

## 🕊️ 朝 — Today’s Goals Auto Selection
- Today の空き時間を入力  
- AI がバックログから今日のタスクを自動抽出  
- 1〜3 個の Today’s Goals を生成

## ⏱️ セッション（PC / BOOK）

### PC 学習セッション
- Start：タイトル・目的・予定時間
- End：自分で短く説明
- AI：
  - 要約  
  - 難所推定  
  - 次やること  
  - 理解度チェック  
  - Zettelkasten ノート生成（MD）

### 本／紙学習セッション
- 書籍情報 → 自分の説明 → AI が整理 + ノート化

## 🌙 夜 — Daily Summary
- 今日のセッション一覧から AI が生成：
  - 今日のまとめ  
  - 目標達成度  
  - 傾向（時間帯など）  
  - 明日のおすすめタスク


# 📚 Zettelkasten Integration（Obsidian）
- AI生成ノートを Markdown として Vault に保存
- notes.py で：
  - 一概念一ノート  
  - 関連リンク生成  
  - タグ付与  
  - メタデータ埋め込み


# 🚀 Development Roadmap（進行プラン）

## Step 1：最低限動く版
- backend：Health / Goals API / Session API（ダミー）
- frontend：最低限の UI
- docker-compose で backend + frontend + postgres 起動

## Step 2：Azureデプロイ
- Terraform で：
  - RG / ACA Env / Backend / Frontend / Postgres
- GitHub Actions で CI/CD

## Step 3：AIロジック実装
- study_core にロジック集約
- LangChain でプロンプト処理
- Obsidian ノート生成

## Step 4：Rust/Go ロガー（将来）
- PCのアクティビティログを追加し、セッション精度を上げる


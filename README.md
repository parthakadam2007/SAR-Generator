SAR-GENERATOR

SAR-Generator/
│
├── README.md
├── package.json              # Root scripts (optional - turborepo/nx)
├── .gitignore
├── .env.example
│
├── frontend/                 # React App
│   ├── package.json
│   ├── vite.config.js
│   ├── tsconfig.json
│   │
│   ├── public/
│   └── src/
│       ├── api/              # API clients
│       ├── auth/
│       ├── components/
│       ├── pages/
│       ├── hooks/
│       ├── store/            # Redux/Zustand
│       ├── routes/
│       ├── styles/
│       └── main.tsx
│
├── backend/
│   │
│   ├── api-gateway/          # Entry Point
│   │   ├── Dockerfile
│   │   ├── nginx.conf
│   │   └── main.go / main.js
│   │
│   ├── main-service/         # Case + Orchestration
│   │   ├── app/
│   │   │   ├── controllers/
│   │   │   ├── services/
│   │   │   ├── models/
│   │   │   └── routes/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── python-ai/            # ML + Detection
│   │   ├── anomaly/
│   │   ├── rules/
│   │   ├── network/
│   │   ├── pipelines/
│   │   ├── app.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   │
│   ├── llm-service/          # LLM Interface
│   │   ├── prompts/
│   │   ├── chains/
│   │   ├── cache/
│   │   ├── main.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
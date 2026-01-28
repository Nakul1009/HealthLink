# HealthLink

### Data Sources → Wearables (APIs) + Reports (PDF/CSV + OCR).
### On-Device Engine → Ingestion → GraphRAG → Personal KG (NetworkX).
### GenAI Layer → Local LLM (AirLLM) + Hybrid RAG (FAISS + KG traversal) → Insights/Queries.
### Anomaly Engine → Lightweight GNNs + rules → Alerts.
### Outputs → User: Chat interface, alerts → Hospital: FHIR export + write-back.
## Key Stack:

### Frontend: React Native / Next.js
### Backend/AI: Python (GraphRAG, FAISS, PyTorch, NetworkX)
### LLM: AirLLM or quantized open models
### Standards: FHIR for interoperability
### Privacy Principle: No cloud sync in MVP; data stays on-device.

# Explainable Federated Analytics for Multivariate Time-Series Forecasting with Personalized Drift Adaptation

## Project Overview
This repository contains the work for **23CSE399 -- Project Phase 1 (Panel Review 1)** at Amrita Vishwa Vidyapeetham. The research focuses on developing a unified federated architecture that integrates personalization, concept drift adaptation, and explainability for multivariate time-series forecasting.

## Key Features
- **Privacy Preservation**: Collaborative model training without centralizing sensitive data.
- **Client Heterogeneity**: Addressing non-IID distributions through a hybrid global–personalized architecture.
- **Concept Drift Adaptation**: Online drift detection using statistical change detection (CUSUM) to trigger adaptive retraining.
- **Explainability**: Attention-based forecasting to provide interpretable predictions.

## Proposed Framework: FPDAF
The **Federated Personalized Drift-Aware Attention Framework (FPDAF)** consists of:
1. **Global Shared Backbone**: Captures common temporal dynamics across clients.
2. **Client-Specific Personalization Layers**: Adapts the model to local data distributions.
3. **Drift-Aware Monitoring Module**: Monitors statistical thresholds to handle evolving environments.

## Repository Structure
- `Team_28/`: Contains the LaTeX source files for the report and presentation.
- `Presentation.pdf`: The project presentation slide deck.
- `Report.pdf`: The detailed project report.

## Team Members (Team 28)
- Sheela Akshar Sakhi (CB.SC.U4CSE23547)
- Hasini Reddy M (CB.SC.U4CSE23529)
- Kousik Sarma Lakkaraju (CB.SC.U4CSE23761)
- Haswitha K (CB.SC.U4CSE23363)
- V.Chakravarthy (CB.SC.U4CSE23753)

## Guides
- Dr. G R RAMYA
- Dr. VANDHANA S

---
*Department of Computer Science and Engineering, Amrita School of Computing.*

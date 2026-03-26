# FPDAF: Explainable Federated Learning for Healthcare Time-Series Forecasting

## Project Overview
This repository contains the evolving work for **23CSE399 -- Project Phase 1** at **Amrita Vishwa Vidyapeetham**. Our research proposes a highly specialized decentralized architecture: the **Federated Personalized Drift-Aware Attention Framework (FPDAF)**. 

The domain of this project is strictly **Healthcare Intensive Care Unit (ICU) Patient Monitoring**, utilizing the **PhysioNet Challenge 2019 (Early Prediction of Sepsis)** multivariate time-series database.

We aim to solve three critical clinical ML challenges:
1.  **Strict Privacy Preservation:** Training deep learning predictive models across entirely siloed hospitals without violating HIPAA/GDPR data-sharing laws.
2.  **Hospital Heterogeneity:** Solving the "Global Model Failure" phenomenon where generalized FedAvg collapses due to distinct regional clinical treatment protocols, solved via **Local Personalization Heads** (FedPer architecture).
3.  **Temporal Patient Deterioration:** Handling rapid physiological degradation over time using continuous **CUSUM Concept Drift Monitoring** tied directly to local attention-driven model retraining.

---

## 🏗 System Architecture & Implementation Logic

### 🏥 Architecture Overview
The framework intentionally decouples the neural network graph. A **Shared Global Temporal Backbone** captures generalized physiological boundaries (e.g., normal adult human heart rates). An extreme **Personalization Head** remains strictly isolated inside the hospital edge server, mapping exact predictions to the local localized cohort distributions. 

![System Architecture](Review%202/images/architecture2.png)

### 📊 Detailed Implementation Logic
Our novel master plan integrates **Decentralization** (global weight syncing via FedAvg), **Customization** (local personalized heads), and **Statistical Math** (active CUSUM monitoring) into a single responsive clinical algorithm.

![Implementation Logic](Review%202/images/FPDAF%20Detailed%20Implementation%20Logic_visul.png)

---

## 🚀 Key Framework Features
- **Decentralization (FedAvg)**: Only encrypted local gradients ($w_{t+1}^k$) are securely uploaded to the central aggregation server.
- **Mathematical Drift Triggers**: Driven by $S_t = \max(0, S_{t-1} + (e_t - \mu - k))$ rather than arbitrary epoch restarts.
- **Interpretable Clinical Analytics**: Time-Series Attention Weights highlight specifically *which historical vital sign spike* (e.g., sudden lack of oxygen saturation) triggered the eventual risk prediction, ensuring XAI transparency for doctors.

---

## 📂 Repository Structure
* **[Implementation/](Implementation/)**: (Phase 2 Initialization)
  * `preprocess_physionet.py`: Automated PyTorch data pipeline for ICU sequence windows.
  * `models.py`: Structural code initializing PyTorch FPDAF modules (LSTM backbone + Local Head).
  * `fed_train.py`: Basic Federated Learning loop simulating PyTorch gradient aggregation.
* **[Review 1/](Review%201/)**: Baseline literature survey mapping 25 peer-reviewed papers.
* **[Review 2/](Review%202/)**: Technical progress and methodology documents.
  * **[images/](Review%202/images/)**: Normalized architectural and implementation diagrams.
  * **[output/](Review%202/output/)**: Final `report.pdf` & `presentation.pdf` compiled natively via LaTeX.
  * **[latex/](Review%202/latex/)**: Bibliography files (`ref.bib`).

---

## 📈 Phase 1 Accomplishments & Phase 2 Roadmap
- [x] **Problem Formulation:** Redefined bounds directly targeting Healthcare Time-Series.
- [x] **Conceptual Architecture:** Finalized the split-server decentralized blueprint.
- [x] **Mathematical Definitions:** Extracted the necessary CUSUM statistical triggers.
- [x] **Baseline Code Initialization:** Bootstrapped the GitHub PyTorch environment.
- [ ] **Phase 2 Pipeline (Pending):** Implement PhysioNet normalization sequences, simulate local PyTorch hospital clients, and rigorously benchmark across (Accuracy, Precision, Recall, F1-Score, and AUC-ROC). 

---

## 👥 Team 28
- Sheela Akshar Sakhi (CB.SC.U4CSE23547)
- Hasini Reddy M (CB.SC.U4CSE23529)
- Kousik Sarma Lakkaraju (CB.SC.U4CSE23761)
- Haswitha K (CB.SC.U4CSE23363)
- V.Chakravarthy (CB.SC.U4CSE23753)

### 🎓 Guides
- **Dr. G R RAMYA**
- **Dr. VANDHANA S**

---
*Department of Computer Science and Engineering, Amrita School of Computing.*

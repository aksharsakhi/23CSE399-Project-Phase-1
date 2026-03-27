# FPDAF: Explainable Federated Learning for Healthcare Time-Series Forecasting

## Project Overview
This repository contains the evolving work for **23CSE399 -- Project Phase 1** at **Amrita Vishwa Vidyapeetham**. Our research proposes a highly specialized decentralized architecture: the **Federated Personalized Drift-Aware Attention Framework (FPDAF)**. 

The domain of this project is strictly **Healthcare Intensive Care Unit (ICU) Patient Monitoring**, utilizing the **PhysioNet Challenge 2019 (Early Prediction of Sepsis)** multivariate time-series database.

We aim to solve three critical clinical ML challenges:
1.  **Strict Privacy Preservation:** Training deep learning predictive models across entirely siloed hospitals without violating HIPAA/GDPR data-sharing laws.
2.  **Hospital Heterogeneity:** Solving the "Global Model Failure" phenomenon where generalized FedAvg collapses due to distinct regional clinical treatment protocols, solved via **Local Personalization Heads** (FedPer architecture).
3.  **Temporal Patient Deterioration:** Handling rapid physiological degradation over time using continuous **CUSUM Concept Drift Monitoring** tied directly to local attention-driven model retraining.

---

## 📊 Data Exploration: 14-Year Longitudinal ICU Stack
To ensure the framework is robust against macro-level data evolution, we have curated a multi-era dataset portfolio spanning **2012--2026** to validate cross-hospital generalizability and drift recovery:

| Era & Source | Dataset Content | Project Validation Role |
| :--- | :--- | :--- |
| **Baseline (2012)** | **PhysioNet 2012**: 12,000 Mortality records | **Age-Robustness:** Validating attention on legacy clinical protocols. |
| **Primary (2019)** | **PhysioNet 2019**: 40,000 Sepsis sequences | **Main Training:** Core FL algorithm & temporal risk forecasting. |
| **High-Fi (2020-21)** | **VitalDB & EDT**: Waveforms & 5s telemetry | **Stress Testing:** Testing CUSUM trigger on sub-minute drifts. |
| **Future (2026)** | **PhysioNet 2026**: Trajectory Flow sources | **State-of-the-Art:** Final validation on the latest clinical standards. |

---

## 🏗 System Architecture & Implementation Logic

### 🏥 Architecture Overview
The framework intentionally decouples the neural network graph. A **Shared Global Temporal Backbone** captures generalized physiological boundaries (e.g., normal adult human heart rates). An extreme **Personalization Head** remains strictly isolated inside the hospital edge server, mapping exact predictions to the local localized cohort distributions. 

![System Architecture](Review%202/images/architecture2.png)

### 📊 Detailed Implementation Logic
Our novel master plan integrates **Decentralization** (global weight syncing via FedAvg), **Customization** (local personalized heads), and **Statistical Math** (active CUSUM monitoring) into a single responsive clinical algorithm.

![Implementation Logic](Review%202/images/FPDAF%20Detailed%20Implementation%20Logic_visul.png)

### 🔍 Research Gap Visual Summary
The following diagram highlights the core limitations identified in existing literature (FedAvg, FedPer) and how the proposed **FPDAF** framework bridges these gaps through integrated explainability and drift adaptation.

![Research Gap Summary](Review%202/images/research_gap_vislu.png)

### 📈 Adaptive System Dataflow
The runtime dataflow processes temporal multivariate arrays sequentially. If the **CUSUM** trigger detects a statistical deviation in prediction residuals, it automatically initiates local personalization.

![System Dataflow](Review%202/images/Dataflow2.png)

---

## 🚀 Key Framework Features
- **Decentralization (FedAvg)**: Only encrypted local gradients ($w_{t+1}^k$) are securely uploaded to the central aggregation server.
- **Mathematical Drift Triggers**: Driven by $S_t = \max(0, S_{t-1} + (e_t - \mu - k))$ rather than arbitrary epoch restarts.
- **Interpretable Clinical Analytics**: Time-Series Attention Weights highlight specifically *which historical vital sign spike* triggered the eventual risk prediction.

---

## 📂 Repository Structure
* **[Implementation/](Implementation/)**: (Phase 2 Initialization)
  * `preprocess_physionet.py`: Automated PyTorch data pipeline for ICU sequence windows.
  * `models.py`: Structural code initializing PyTorch FPDAF modules (LSTM backbone + Local Head).
  * `fed_train.py`: Basic Federated Learning loop simulating PyTorch gradient aggregation.
* **[Review 1/](Review%201/)**: Baseline literature survey mapping 25 peer-reviewed papers.
  * **[Full Literature Analysis (25+ Papers)](https://docs.google.com/spreadsheets/d/1G_zAbr6MI_bYcCHEXfkWjhmvKzBEDKr0/edit#gid=417550448)**: Detailed Google Sheets analysis.
* **[Review 2/](Review%202/)**: Technical progress and methodology documents.
  * **[images/](Review%202/images/)**: Normalized architectural and implementation diagrams.
  * **[output/](Review%202/output/)**: Final `report.pdf` & `presentation.pdf`.
  * **[latex/](Review%202/latex/)**: Bibliography files (`ref.bib`).

---

## 👥 Team 28
- **SHEELA AKSHAR SAKHI** (CB.SC.U4CSE23547)
- **HASINI REDDY M** (CB.SC.U4CSE23529)
- **KOUSIK SARMA LAKKARAJU** (CB.SC.U4CSE23761)
- **HASWITHA K** (CB.SC.U4CSE23363)
- **V. CHAKRAVARTHY** (CB.SC.U4CSE23753)

### 🎓 Guides
- **DR. G R RAMYA**
- **DR. VANDHANA S**

---
*Department of Computer Science and Engineering, Amrita School of Computing.*

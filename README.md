# FPDAF: Explainable Federated Learning for Healthcare Time-Series Forecasting

## Project Overview
This repository contains the work for **23CSE399 -- Project Phase 1** at **Amrita Vishwa Vidyapeetham**. Our research proposes the **Federated Personalized Drift-Aware Attention Framework (FPDAF)**, a decentralized architecture designed for early ICU risk prediction.

### 🏥 Clinical Context & Terminology
- **Sepsis:** Life-threatening organ failure caused by infection; needs early detection.
- **Deterioration:** Rapid worsening of patient condition (vitals becoming abnormal).
- **Profiling:** Analyzing time-series data (Heart Rate, BP) to predict patient risk.

### 🔍 Motivation: The Three Gaps
We aim to solve three critical clinical challenges:
1.  **The Privacy Gap:** Strict laws (**HIPAA/DPDPA**) prevent hospitals from sharing raw patient data to a central cloud.
2.  **The Accuracy Gap:** Standard "one-size-fits-all" AI fails because every hospital has different patient types and local protocols.
3.  **The Trust Gap:** Doctors cannot trust "black-box" AI alerts; they need explainable proof (**XAI**) to make life-saving decisions.

### 🌍 Sustainable Development Goal (SDG) Mapping
- **Primary (SDG 3):** Directly contributes to **Good Health and Well-being** by enabling explainable patient risk prediction.
- **Secondary (SDG 9 & 16):** Supports scalable clinical innovation and ethical data privacy security.

---

## 🏗 System Architecture (Master Visual)
The framework decoupling the neural network graph to ensure both global intelligence and local privacy.

![Master Architecture](Review%202/images/ArcDigram.jpeg)

---

## 📅 Phase 2 & 3 Roadmap (2026-2027)

| Target Area | Objective for Phase 2 & 3 | Tentative Time |
| :--- | :--- | :--- |
| **Data Preprocessing** | Clean, Impute, and construct sequential windows. | **Ongoing -- April 2026** |
| **Baseline Training** | Code standard FedAvg on PyTorch for baselines. | **April -- June 2026** |
| **FPDAF Integration** | Embed CUSUM triggers and Attention layers. | **July -- Sept 2026** |
| **Federated Simulation** | Deploy simulated Hospital "Clients" to test latency. | **Oct -- Dec 2026** |
| **Final Evaluation** | Overall system performance benchmarking (AUC-ROC). | **Jan -- Feb 2027** |

---

## 🚀 Key Innovation Pillars
- **Novel FedAvg Extension:** Uses **Attention-Aware Weighting** to prioritize higher-confidence hospital data.
- **Novel CUSUM Extension:** Repurposes statistical monitoring as an active **Automated Neural Trigger**.
- **Novel Local Personalization:** Extends standard **FedPer** nodes to handle hospital-specific demographics.

---

## 📂 Repository Structure
* **[Review 2/](Review%202/)**: Technical progress and methodology documents.
  * **[images/](Review%202/images/)**: Normalized architectural and implementation diagrams.
  * **[output/](Review%202/output/)**: Final `report.pdf` & `presentation.pdf`.
* **[Implementation/](Implementation/)**: (Phase 2 Initialization)
* **[Review 1/](Review%201/)**: Baseline literature survey mapping 25 peer-reviewed papers.

---

## 👥 Team 28
- **SHEELA AKSHAR SAKHI** (CB.SC.U4CSE23547)
- **HASINI REDDY M** (CB.SC.U4CSE23529)
- **KOUSIK SARMA LAKKARAJU** (CB.SC.U4CSE23761)
- **HASWITHA K** (CB.SC.U4CSE23363)
- **V. CHAKRAVARTHY** (CB.SC.U4CSE23753)

### 🎓 Guides: DR. G R RAMYA & DR. VANDHANA S
*Department of Computer Science and Engineering, Amrita School of Computing.*

# Detailed Literature Survey Summary

This document summarizes the literature review conducted for the **FPDAF (Federated Personalized Drift-Aware Attention Framework)** project. A total of 25 papers were analyzed focusing on Federated Learning, Personalization, Concept Drift, and Explainable AI.

## Key Research Gaps Identified

- **Personalization vs. Interpretability**: Most personalized FL models lack explainability.
- **Online Drift Detection**: Monitoring distribution shifts within federated loops is rare.
- **Multivariate Forecasting**: Limited exploration of complex multivariate time-series in federated settings.
- **Dynamic Environments**: Most studies assume steady-state data distributions.

## Overview of Reviewed Papers

### Paper 1: A standalone software for real-time facial analysis in online conferences and e-lessons

- **Publisher/Year**: Elsevier (Software Impacts) (2023)
- **Methodology**: MTCNN face detection; EfficientNet-B0 for face recognition & FER; Apache TVM optimization; L2 embedding-based tracking
- **Advantage**: Cross-platform; lightweight; real-time; CSV logs
- **Disadvantage**: Old MTCNN model performs poorly; no engagement score; only numeric IDs
- **Research Gap**: Replace MTCNN with modern detector; add engagement estimation; integrate OCR for user names; improve user-specific FER accuracy
- **Relevance**: Relates to Layer-1 and Layer-2 , Shows how analytics and ML models run locally on devices without sharing raw data, Supports local insights, privacy preservation, and on-device intelligence
- **Link**: [https://doi.org/10.1016/j.simpa.2023.100507](https://doi.org/10.1016/j.simpa.2023.100507)

---

### Paper 2: Concept drift detection and adaptation for federated and continual learning (CDA-FedAvg)

- **Publisher/Year**: Springer (Multimedia Tools and Applications) (2022)
- **Methodology**: CUSUM-type drift detection; Beta-distribution comparison; Short & long-term memory; Asynchronous Federated Averaging
- **Advantage**: Unsupervised drift detection; handles sudden/gradual drifts; lower communication load
- **Disadvantage**: Hyperparameter sensitivity (Nmax); higher computation; memory grows with concepts
- **Research Gap**: Use deep drift detectors; optimize window parameters; add personalized FL adaptation; extend to multimodal datasets
- **Relevance**: Directly matches full project architecture , Solves client heterogeneity, concept drift, federated aggregation, adaptation over time, privacy-preserving collaboration, Demonstrates local learning + global updates + drift detection exactly like our 3-layer architecture
- **Link**: [https://doi.org/10.1007/s11042-021-11219-x](https://doi.org/10.1007/s11042-021-11219-x)

---

### Paper 3: Federated Learning with Personalization Layers (FedPer)

- **Publisher/Year**: Elsevier / AISTATS (Scopus indexed) (2020)
- **Methodology**: Splits model into global base layers and local personalized layers; Base layers trained using FedAvg; Personalized layers trained locally; CNN-based architectures
- **Advantage**: Strong personalization; Handles client heterogeneity; Privacy preserved
- **Disadvantage**: No concept drift handling; Requires careful layer separation
- **Research Gap**: Add drift-aware personalization for time-series forecasting
- **Relevance**: Solves one-model-does-not-fit-all problem; Matches Layer-2 personalized forecasting in our project
- **Link**: [https://proceedings.mlr.press/v108/arivazhagan20a.html](https://proceedings.mlr.press/v108/arivazhagan20a.html)

---

### Paper 4: Communication-Efficient Learning of Deep Networks from Decentralized Data

- **Publisher/Year**: AISTATS / PMLR (Scopus indexed) (2017)
- **Methodology**: Local SGD on clients; Multiple local epochs per round; Partial client participation; Server-side model averaging
- **Advantage**: Foundation of federated learning; Strong privacy preservation
- **Disadvantage**: No personalization; No drift handling; No explainability
- **Research Gap**: Extend FedAvg with personalization, analytics, and drift detection
- **Relevance**: Forms Layer-3 backbone of our project; Enables privacy-preserving global aggregation
- **Link**: [https://proceedings.mlr.press/v54/mcmahan17a.html](https://proceedings.mlr.press/v54/mcmahan17a.html)

---

### Paper 5: Federated Learning with Dual-End Gradient Correction and Proxy-Free Self-Distillation

- **Publisher/Year**: IEEE Access (Scopus indexed) (2022)
- **Methodology**: Dual-end gradient correction; Proxy-free self-distillation; Reduces client drift; Optimized for non-IID data
- **Advantage**: Handles client drift; No raw data sharing
- **Disadvantage**: Higher computation cost; Lacks explainability
- **Research Gap**: Add explainable analytics and time-series forecasting support
- **Relevance**: Addresses client heterogeneity and aggregation instability in our project
- **Link**: [https://doi.org/10.1109/ACCESS.2022.3140096](https://doi.org/10.1109/ACCESS.2022.3140096)

---

### Paper 6: MVFL — Multivariate Vertical Federated Learning for Time-Series Forecasting

- **Publisher/Year**: IFIP (via CNSM 2025 Conference Proceedings) (2025)
- **Methodology**: Introduces MVFL, a vertical federated learning framework that separates local and shared features to enable efficient multivariate time-series forecasting on distributed edge devices.
- **Advantage**: Highly resource-efficient and well-suited for IoT and edge-based multivariate time-series data.
- **Disadvantage**: Does not incorporate explainability or personalized model adaptation across clients.
- **Research Gap**: Lacks explainable analytics and client-specific personalization, which are critical for trust and heterogeneous data settings.
- **Relevance**: Forms the core federated and multivariate forecasting backbone for our proposed explainable and personalized framework.
- **Link**: [https://ieeexplore.ieee.org/document/11297529](https://ieeexplore.ieee.org/document/11297529)

---

### Paper 7: FedXAI : Federated Learning of Explainable AI for Intrusion Detection

- **Publisher/Year**: Elsevier – Computer Networks Journal (2025)
- **Methodology**: Combines federated learning with explainable AI by aggregating SHAP-based explanations from clients without sharing raw data.
- **Advantage**: Provides privacy-preserving explainability, increasing transparency and trust in federated models.
- **Disadvantage**: Focused on classification tasks rather than time-series forecasting.
- **Research Gap**: Explainability is not extended to multivariate time-series forecasting scenarios
- **Relevance**: Provides the explainability mechanism that can be adapted for federated time-series forecasting.
- **Link**: [https://www.sciencedirect.com/science/article/pii/S1389128625004463](https://www.sciencedirect.com/science/article/pii/S1389128625004463)

---

### Paper 8: Federated Learning for Financial Forecasting

- **Publisher/Year**: ETH Zurich Technical Report / arXiv (2025)
- **Methodology**: Applies federated learning with LSTM models on non-IID financial time-series and evaluates personalization through fine-tuning.
- **Advantage**: Strong demonstration of personalization benefits in federated time-series learning.
- **Disadvantage**: Limited to binary trend prediction instead of multivariate forecasting.
- **Research Gap**: Personalization is not explored for multivariate or explainable forecasting tasks.
- **Relevance**: Supports the personalized model adaptation component of our proposed framework
- **Link**: [https://arxiv.org/pdf/2509.16393](https://arxiv.org/pdf/2509.16393)

---

### Paper 9: Privacy-Preserving Clinical Decision Support for Emergency Triage Using LLMs

- **Publisher/Year**: MDPI (Scopus Indexed) (2025)
- **Methodology**: Integrates federated learning, large language models, and secure aggregation for real-time clinical decision support.
- **Advantage**: Demonstrates real-world deployment feasibility of FL in sensitive healthcare settings.
- **Disadvantage**: System complexity and high computational requirements.
- **Research Gap**: Explainable and personalized forecasting for clinical time-series is not addressed.
- **Relevance**: Provides application-level motivation for explainable and personalized federated analytics.
- **Link**: [https://www.mdpi.com/2076-3417/15/15/8412](https://www.mdpi.com/2076-3417/15/15/8412)

---

### Paper 10: Personalized Federated Learning for Time-Series Forecasting(Building Energy)

- **Publisher/Year**: Elsevier / ACM (2024-2025)
- **Methodology**: Uses shared global models with client-specific heads or fine-tuning to handle heterogeneous time-series data
- **Advantage**: Effectively adapts federated models to local client characteristics.
- **Disadvantage**: Increases model and training complexity.
- **Research Gap**: Does not combine personalization with explainability and multivariate forecasting.
- **Relevance**: Directly contributes to the personalized adaptation aspect of our work.
- **Link**: [https://www.sciencedirect.com/science/article/pii/S0378778824008788](https://www.sciencedirect.com/science/article/pii/S0378778824008788)

---

### Paper 11: A Federated Large Language Model for Long-Term Time Series Forecasting

- **Publisher/Year**: arXiv (2024)
- **Methodology**: Federated learning framework using a pre-trained Large Language Model (LLaMA) for long-term time series forecasting; client-side local training with parameter-efficient fine-tuning; K-means clustering of clients to reduce data bias; channel independence and patching to preserve temporal semantics.
- **Advantage**: Preserves data privacy using federated learning; effectively captures long-range temporal dependencies; reduces communication and computational cost using parameter-efficient tuning.
- **Disadvantage**: High computational complexity due to LLM backbone; requires substantial resources on edge devices; limited evaluation on extremely resource-constrained clients.
- **Research Gap**: Does not address adaptive personalization for highly heterogeneous client time series; scalability issues remain for large numbers of low-power devices.
- **Relevance**: This paper supports federated long-term time series forecasting while preserving privacy, aligning with decentralized and privacy-aware prediction objectives.
- **Link**: [https://doi.org/10.48550/arXiv.2407.20503](https://doi.org/10.48550/arXiv.2407.20503)

---

### Paper 12: FedForecaster: An Automated Federated Learning Approach for Time-series Forecasting

- **Publisher/Year**: EDBT Conference (2025)
- **Methodology**: Automated federated learning framework for time series forecasting; meta-learning-based algorithm selection using aggregated statistical meta-features; Bayesian optimization for hyperparameter tuning; client-side automated feature engineering without data sharing.
- **Advantage**: Fully automated forecasting pipeline; preserves data privacy; reduces human effort in model selection and tuning; adaptable to heterogeneous client data.
- **Disadvantage**: Focused only on univariate time series; additional overhead due to meta-feature computation; limited evaluation on multivariate datasets.
- **Research Gap**: Does not address multivariate or personalized forecasting; lacks mechanisms for handling extreme non-IID data distributions across clients.
- **Relevance**: This work aligns with privacy-preserving federated forecasting and highlights the need for adaptive, automated solutions under heterogeneous data conditions.
- **Link**: [https://www.openproceedings.org/2025/conf/edbt/paper-266.pdf](https://www.openproceedings.org/2025/conf/edbt/paper-266.pdf)

---

### Paper 13: Privacy-Enhancing Federated Time-Series Forecasting: A Microaggregation-Based Approach

- **Publisher/Year**: SECRYPT (2025)
- **Methodology**: Federated learning framework enhanced with microaggregation for privacy; k-anonymity applied on client-side time series; aggregation of anonymized data representations; evaluation under different privacy levels.
- **Advantage**: Strong privacy guarantees; flexible privacy-utility trade-off; compatible with lightweight client-side models.
- **Disadvantage**: Information loss due to aggregation; reduced accuracy for highly dynamic time series; additional preprocessing overhead.
- **Research Gap**: Does not address data heterogeneity or personalization; limited scalability analysis for large federated systems.
- **Relevance**: This paper emphasizes privacy preservation in federated time series forecasting, which is a key requirement in decentralized analytics systems.
- **Link**: [https://www.scitepress.org/publishedPapers/2025/136411/pdf/index.html](https://www.scitepress.org/publishedPapers/2025/136411/pdf/index.html)

---

### Paper 14: Tackling Data Heterogeneity in Federated Time Series Forecasting

- **Publisher/Year**: arXiv (2024)
- **Methodology**: Fed-TREND framework to handle heterogeneous time series data; generation of synthetic data from client and global model trajectories; auxiliary data used to enhance local training and global aggregation; compatible with multiple forecasting models.
- **Advantage**: Effectively addresses data heterogeneity; model-agnostic framework; improves generalization across diverse clients.
- **Disadvantage**: Synthetic data generation adds computational overhead; depends on the quality of model updates; increased server-side complexity.
- **Research Gap**: Does not provide theoretical guarantees for optimal horizon selection; limited personalization for client-specific dynamics.
- **Relevance**: Directly addresses federated time series forecasting under heterogeneous data distributions, aligning with decentralized analytics objectives.
- **Link**: [https://doi.org/10.48550/arXiv.2411.15716](https://doi.org/10.48550/arXiv.2411.15716)

---

### Paper 15: Optimal Look-back Horizon for Time Series Forecasting in Federated Learning

- **Publisher/Year**: AAAI / arXiv (2025)
- **Methodology**: Theoretical framework for adaptive horizon selection in federated time series forecasting; intrinsic space formulation; synthetic data generator modeling temporal structures; loss decomposition into Bayesian and approximation errors.
- **Advantage**: Strong theoretical foundation; client-adaptive horizon selection; improves model efficiency and generalization.
- **Disadvantage**: Complex mathematical formulation; limited real-world deployment evaluation; assumes structured temporal patterns.
- **Research Gap**: Practical adaptive horizon selection for real-time federated systems; integration with personalized federated models.
- **Relevance**: Supports efficient and adaptive federated time series forecasting by optimizing historical context under heterogeneous data settings.
- **Link**: [https://doi.org/10.48550/arXiv.2511.12791](https://doi.org/10.48550/arXiv.2511.12791)

---

### Paper 16: Federated Multi-Task Learning for Time Series Forecasting

- **Publisher/Year**: IEEE Transactions on Neural Networks and Learning Systems (2022)
- **Methodology**: Treats each client as a related forecasting task
Uses shared global representation + task-specific parameters
Joint optimization via federated multi-task learning
Handles non-IID client distributions
- **Advantage**: Strong personalization without sharing raw data
- **Disadvantage**: No built-in explainability mechanism
- **Research Gap**: Lacks interpretability for model decisions

No analytics-level explanations for stakeholders
- **Relevance**: Provides personalized federated forecasting, which you can extend with explainable analytics.
- **Link**: [https://www.researchgate.net/publication/371352969_Forecasting_Functional_Time_Series_Using_Federated_Learning](https://www.researchgate.net/publication/371352969_Forecasting_Functional_Time_Series_Using_Federated_Learning)

---

### Paper 17: Interpretable Multivariate Time-Series Forecasting with Attention Mechanisms

- **Publisher/Year**: NeurIPS (2021)
- **Methodology**: Attention-based encoder–decoder
Temporal + variable-level attention
Multivariate dependency modeling
- **Advantage**: Strong explainability for multivariate forecasting
- **Disadvantage**: Centralized (not federated)
- **Research Gap**: No privacy-preserving or federated setting
- **Relevance**: Supplies the explainability backbone you can integrate into federated analytics.
- **Link**: [https://www.mdpi.com/2673-2688/6/6/117](https://www.mdpi.com/2673-2688/6/6/117)

---

### Paper 18: Federated Learning under Heterogeneous Time Series Data

- **Publisher/Year**: ACM SIGKDD (2023)
- **Methodology**: Clustered client grouping
Client similarity measurement
Cluster-wise model aggregation
- **Advantage**: Handles severe heterogeneity effectively
- **Disadvantage**: No user-level personalization inside clusters
- **Research Gap**: No personalized explainability per client
- **Relevance**: Supports heterogeneous federated analytics, a key challenge in your system.
- **Link**: [https://dl.acm.org/doi/10.1145/3580305.3599354](https://dl.acm.org/doi/10.1145/3580305.3599354)

---

### Paper 19: Explainable AI for Multivariate Time Series Forecasting

- **Publisher/Year**: Elsevier – Information Sciences (2022)
- **Methodology**: SHAP-based explanation
Feature-wise contribution analysis
Model-agnostic interpretability
- **Advantage**: Model-agnostic explainability
- **Disadvantage**: High computational overhead
- **Research Gap**: Not designed for federated environments
- **Relevance**: Provides explainable analytics, which you extend to federated forecasting.
- **Link**: [https://www.mdpi.com/2673-2688/6/6/117](https://www.mdpi.com/2673-2688/6/6/117)

---

### Paper 20: Personalized Federated Learning with Adaptive Model Fusion

- **Publisher/Year**: AAAI (2023)
- **Methodology**: Adaptive weighting of global & local models

Client-level model fusion

Personalized update strategies
- **Advantage**: Strong personalization capability
- **Disadvantage**: No domain-specific explainability
- **Research Gap**: No analytical explanation for predictions
- **Relevance**: Directly supports personalized model adaptation in federated analytics.
- **Link**: [https://www.sciencedirect.com/science/article/abs/pii/S0957417424011692](https://www.sciencedirect.com/science/article/abs/pii/S0957417424011692)

---

### Paper 21: Early Sepsis Onset Prediction Through Federated Learning

- **Publisher/Year**: ArXiv (2025)
- **Methodology**: Sliding Window+Federated Strategy
- **Advantage**: Early Warning Optimised for predicting sepsis hours before it happens, giving doctors time to act.
- **Disadvantage**: Black Box It focuses purely on accuracy numbers (F1-score) without explaining why a patient is at risk.
- **Research Gap**: Lack of Explainability: The model predicts risk but doesn't explain the medical reasons. (We will add the Explanation Layer).
- **Relevance**: Layer 1: Validates use of LSTMs for time-series forecasting.
- **Link**: [https://arxiv.org/pdf/2509.20885](https://arxiv.org/pdf/2509.20885)

---

### Paper 22: FedSepsis: A Federated Multi-Modal Deep Learning-Based Application

- **Publisher/Year**: MDPI (2023)
- **Methodology**: Edge Computing+GANs+Multimodal
- **Advantage**: Low Cost Hardware Proves the system can run on cheap IoT devices (Raspberry Pi), suitable for rural clinics.
- **Disadvantage**: High Computation Running GANs on a Raspberry Pi is very heavy and slow for real-time alerts
- **Research Gap**: Computation Load:GANs are too heavy for simple alerts.
- **Relevance**: Hardware: Proves system works on Hospital IoT/Edge devices.
- **Link**: [https://www.mdpi.com/1424-8220/23/2/970](https://www.mdpi.com/1424-8220/23/2/970)

---

### Paper 23: Supervised ML Models for Predicting Sepsis & Decision Support

- **Publisher/Year**: JMIR Med (2025)
- **Methodology**: Stacking Ensemble SHAP ValuesFeature Ranking
- **Advantage**: Trust: Shows doctors specific risk factors (e.g., Low BP).
- **Disadvantage**: Not FederatedCentralized data only (Privacy risk).
- **Research Gap**: Privacy Risk: Good explanations, bad privacy (We combine XAI + FL).
- **Relevance**: Layer 3 (Explainability): Provides the logic for your "Insights" layer (using SHAP/Feature Importance).
- **Link**: [https://www.jmir.org/2025/1/e66733](https://www.jmir.org/2025/1/e66733)

---

### Paper 24: MultiProg: Privacy-Preserving FL Framework

- **Publisher/Year**: PMC (2025)
- **Methodology**: Multi-Channel ArchFeature Calibration
Dynamic Weighting
- **Advantage**: Robust: Works even if hospitals have different data formats.
- **Disadvantage**: Complex: Hard to implement multi-channel syncing.
- **Research Gap**: No Automation: No auto-alerts for nurses. (We add Auto-Reporting).
- **Relevance**: Layer 2 (Personalization): Solves the "Kerala vs. Delhi" data difference problem.
- **Link**: [https://pmc.ncbi.nlm.nih.gov/articles/PMC12031511/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12031511/)

---

### Paper 25: Federated Learning for Severity Classification (Secure Edge)

- **Publisher/Year**: IEEE Access (2025)
- **Methodology**: Secure MPC Adaptive Thresholding
Edge Aggregation
- **Advantage**: Security: Server cannot see raw model weights.
- **Disadvantage**: Slow: Encryption adds training delay.
- **Research Gap**: No GenAI: Secure but not user-friendly. (We add LLM interface).
- **Relevance**: Security: Reinforces your "Privacy-Preserving" claim with advanced encryption.
- **Link**: [https://ieeexplore.ieee.org/document/11021594/](https://ieeexplore.ieee.org/document/11021594/)

---

### Paper 1: Egor Churaev et al., Elsevier (Software Impacts), 2023

- **Publisher/Year**: MTCNN face detection; EfficientNet-B0 for FER; Apache TVM optimization; L2 embedding-based tracking (Real-time on-device facial analysis without sharing raw data)
- **Methodology**: No federated learning; no personalization; no drift handling
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 2: Jothimurugesan et al., Springer (Multimedia Tools and Applications), 2022

- **Publisher/Year**: CDA-FedAvg with CUSUM drift detection; short & long-term memory (Concept drift detection and adaptation in federated learning)
- **Methodology**: Higher computation; parameter sensitivity; no time-series forecasting focus
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 3: Arivazhagan et al., Elsevier / AISTATS, 2020

- **Publisher/Year**: FedPer with shared base layers and local personalized layers (Personalized federated learning for heterogeneous clients)
- **Methodology**: No drift detection; no analytics layer
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 4: McMahan et al., PMLR / AISTATS, 2017

- **Publisher/Year**: FedAvg using local SGD and global model averaging (Privacy-preserving decentralized model training)
- **Methodology**: No personalization; no explainability; no drift handling
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 5: Liu et al., IEEE Access, 2022

- **Publisher/Year**: Dual-end gradient correction with proxy-free self-distillation (Stable and optimized federated learning under non-IID data)
- **Methodology**: Lacks explainability; not time-series focused
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 6: HASINI REDDY.M, IFIP (CNSM Conference Proceedings), 2025

- **Publisher/Year**: MVFL framework; separation of local and shared features; vertical federated learning; FedAvg-style aggregation (Multivariate time-series forecasting using vertical federated learning on edge/IoT devices)
- **Methodology**: No explainability; no client-specific personalization
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 7: HASINI REDDY.M, Elsevier (Computer Networks Journal), 2025

- **Publisher/Year**: FedXAI with FedAvg aggregation; SHAP and LIME-based explanations (Privacy-preserving explainable AI in federated intrusion detection)
- **Methodology**: Focused on classification; not applied to time-series forecasting
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 8: HASINI REDDY.M, ETH Zurich / arXiv, 2025

- **Publisher/Year**: Federated LSTM models; FedAvg aggregation; client-side fine-tuning (Personalized federated learning for financial time-series forecasting)
- **Methodology**: Limited to binary trend prediction; no multivariate forecasting
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 9: HASINI REDDY.M, MDPI (Scopus Indexed), 2025

- **Publisher/Year**: Federated learning with LLMs; secure aggregation; real-time clinical decision support (Privacy-preserving clinical decision support in healthcare)
- **Methodology**: High system complexity; no personalized time-series explainability
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 10: HASINI REDDY.M, Elsevier / ACM, 2024–2025

- **Publisher/Year**: Shared global model with client-specific heads; FedAvg-based personalization (Personalized federated learning for time-series forecasting)
- **Methodology**: Increased training complexity; lacks explainability
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 11: K. Haswitheswari, arXiv, 2024

- **Publisher/Year**: Federated learning with Large Language Models (LLaMA); parameter-efficient fine-tuning; client clustering; channel independence (Long-term federated time-series forecasting with privacy preservation)
- **Methodology**: High computational cost; limited suitability for low-resource edge devices
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 12: K. Haswitheswari, EDBT Conference, 2025

- **Publisher/Year**: AutoML-based federated learning; meta-feature aggregation; Bayesian optimization; automated feature engineering (Automated federated time-series forecasting)
- **Methodology**: Limited to univariate time series; overhead from meta-feature computation
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 13: K. Haswitheswari, SECRYPT, 2025

- **Publisher/Year**: Microaggregation with k-anonymity; federated learning aggregation (Privacy-enhanced federated time-series forecasting)
- **Methodology**: Information loss due to aggregation; reduced accuracy for dynamic data
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 14: K. Haswitheswari, arXiv, 2024

- **Publisher/Year**: Fed-TREND framework; synthetic data generation; heterogeneity-aware aggregation (Handling data heterogeneity in federated time-series forecasting)
- **Methodology**: Computational overhead; limited personalization
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 15: K. Haswitheswari, AAAI / arXiv, 2025

- **Publisher/Year**: Adaptive look-back horizon selection; intrinsic space formulation; loss decomposition (Optimizing historical context in federated time-series forecasting)
- **Methodology**: Complex theoretical formulation; limited real-world deployment
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 16: V. Chakravarthy, IEEE Transactions on Neural Networks and Learning Systems, 2022

- **Publisher/Year**: Federated multi-task learning; shared global representation; task-specific parameters; joint optimization (Personalized federated time-series forecasting under non-IID data)
- **Methodology**: No built-in explainability mechanism
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 17: V. Chakravarthy, NeurIPS, 2021

- **Publisher/Year**: Attention-based encoder–decoder; temporal and variable-level attention; multivariate dependency modeling (Interpretable multivariate time-series forecasting)
- **Methodology**: Centralized approach; not federated
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 18: V. Chakravarthy, ACM SIGKDD, 2023

- **Publisher/Year**: Client clustering; similarity-based grouping; cluster-wise model aggregation (Handling heterogeneous time-series data in federated learning)
- **Methodology**: No per-client personalization inside clusters
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 19: V. Chakravarthy, Elsevier (Information Sciences), 2022

- **Publisher/Year**: SHAP and LIME explanations; model-agnostic interpretability; feature-wise contribution analysis (Explainable AI for multivariate time-series forecasting)
- **Methodology**: High computational overhead; not federated
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 20: V. Chakravarthy, AAAI, 2023

- **Publisher/Year**: Adaptive model fusion; client-level weighting of global and local models (Personalized federated learning under heterogeneous data)
- **Methodology**: No domain-specific explainability
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 21: Kousik Sarma, arXiv, 2025

- **Publisher/Year**: Sliding-window strategy with federated learning; Attention-LSTM; FedAvg aggregation (Early sepsis onset prediction using federated time-series learning)
- **Methodology**: Black-box predictions; lacks medical explainability
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 22: Kousik Sarma, MDPI, 2023

- **Publisher/Year**: Edge computing with CNN-LSTM; GAN-based data augmentation; federated learning (Federated multimodal sepsis detection on edge/IoT devices)
- **Methodology**: High computation due to GANs; slow real-time alerts
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 23: Kousik Sarma, JMIR Medical Informatics, 2025

- **Publisher/Year**: Stacking ensemble (XGBoost); SHAP-based feature importance; centralized learning (Explainable clinical decision support for sepsis risk)
- **Methodology**: Not federated; privacy risk due to centralized data
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 24: Kousik Sarma, PMC, 2025

- **Publisher/Year**: Multi-channel federated learning; feature calibration; dynamic weighting (Privacy-preserving federated learning across heterogeneous hospitals)
- **Methodology**: Complex synchronization; no automated alerting
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---

### Paper 25: Kousik Sarma, IEEE Access, 2025

- **Publisher/Year**: Secure multi-party computation; adaptive thresholding; encrypted FedAvg (Secure federated learning for severity classification at the edge)
- **Methodology**: Training delay due to encryption; no user-friendly interface
- **Advantage**: N/A
- **Disadvantage**: N/A
- **Research Gap**: N/A
- **Relevance**: N/A
- **Link**: N/A

---


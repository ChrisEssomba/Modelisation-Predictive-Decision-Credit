# 💳 Prédiction des Décisions de Crédit Bancaire grace au Machine Learning

## 🎯 Introduction

La gestion des décisions de crédit est un **enjeu stratégique majeur** pour les institutions financières. Elle conditionne leur capacité à **minimiser les risques**, à **allouer efficacement les ressources** et à maintenir la **confiance des investisseurs**.

Dans ce contexte, l’analyse et la **prédiction automatique** des décisions de crédit jouent un rôle crucial pour **évaluer la solvabilité** des demandeurs et automatiser une partie du processus décisionnel.

🔍 Ce projet a pour objectif de :

- Identifier les **facteurs déterminants** dans l’octroi ou le refus d’un prêt.
- Développer un **modèle prédictif fiable** afin d'assister les banques dans la prise de décision.
- Intégrer ce modèle dans une **application web simple** à utiliser.

---

## 🧠 Modélisation & Choix du Modèle

Trois modèles de classification ont été comparés :

- **Régression Logistique**
- **K-Nearest Neighbors**
- **Decision Tree Classifier**

Après entraînement et évaluation, le **Decision Tree Classifier** a été retenu avec une **précision de 92%**, surpassant les autres modèles. Ce choix s’explique par :

- Sa **performance élevée** sur nos données.
- Sa **simplicité d’interprétation**, essentielle dans le secteur bancaire où la transparence du modèle est souvent requise.
- Sa capacité à **gérer les interactions non linéaires** entre les variables explicatives.

Le modèle a ensuite été sauvegardé (`model.pkl`) et intégré dans une application web développée avec **Flask**.

---

## ⚙️ Technologies utilisées

- **Python 3**
- **Pandas**, **Scikit-learn**, **Matplotlib**, **Seaborn**
- **Flask** (déploiement web)
- **Jupyter Notebook**
- **Git / GitHub**

---

## 🌐 Application Web

Une interface simple permet à l'utilisateur de :

- Saisir les caractéristiques d’un demandeur de prêt.
- Obtenir instantanément la **décision prédite** (accord ou refus).
- Visualiser la probabilité associée à la prédiction.

Cette interface peut facilement être adaptée pour un usage réel dans un contexte bancaire ou éducatif.

---

## 📦 Installation & Lancement

1. Cloner le dépôt :

```bash
git clone https://github.com/votre-utilisateur/loan-prediction-app.git
cd loan-prediction-app
```

2. Installer les dépendances :

```bash
pip install -r requirements.txt
```

3. Lancer l’application Flask :

```bash
cd Application
python app.py
```

Accéder à l’application sur : http://localhost:5000

## 📊 Rapport & Analyse

Le RapportDeProjet.pdf contient :

- **Une analyse exploratoire des données (corrélations, outliers, distributions)**
- **Une explication des choix de modélisation**
- **Une comparaison des performances**
- **Des recommandations pour améliorer le modèle ou l’adapter à de nouvelles données**

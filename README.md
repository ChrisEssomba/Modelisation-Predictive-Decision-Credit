# 💳 Prédiction des Décisions de Crédit Bancaire avec Machine Learning

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

## 🗂️ Structure du projet

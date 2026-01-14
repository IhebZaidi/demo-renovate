# 🚀 Application FastAPI - Démo Renovate

Application de démonstration utilisant FastAPI avec des **versions anciennes volontaires** pour illustrer le fonctionnement de Renovate.

## 📦 Dépendances (anciennes)

- **FastAPI**: 0.95.0 → Dernière: 0.115.0+
- **Python**: 3.9.16 → Dernière: 3.13.x
- **PostgreSQL**: 14.7 → Dernière: 17.x
- **SQLAlchemy**: 1.4.46 → Dernière: 2.0.x
- **Pydantic**: 1.10.5 → Dernière: 2.x

## 🚀 Installation et Démarrage

### Avec Docker Compose (recommandé)

```bash
# Démarrer l'application
docker-compose up --build

# Accéder à l'application
# API: http://localhost:8000
# Documentation: http://localhost:8000/docs
```

### Sans Docker

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Installer les dépendances
pip install -r requirements.txt

# Démarrer l'application
python -m app.main
```

## 🧪 Tests

```bash
pytest tests/ -v
```

## 🔄 Renovate

Une fois Renovate activé sur votre dépôt, il va :

1. ✅ Détecter les 15+ dépendances obsolètes
2. ✅ Créer des PR groupées selon la configuration
3. ✅ Proposer la mise à jour de Python 3.9 → 3.13
4. ✅ Mettre à jour FastAPI 0.95 → 0.115+
5. ✅ Upgrader PostgreSQL 14 → 17
6. ✅ Auto-merger les patches de tests après CI

## 📊 Endpoints API

- `GET /` - Informations générales
- `GET /health` - Health check
- `POST /api/v1/users/` - Créer un utilisateur
- `GET /api/v1/users/` - Liste des utilisateurs
- `GET /api/v1/users/{id}` - Détails utilisateur
- `POST /api/v1/items/` - Créer un item
- `GET /api/v1/items/` - Liste des items
- `GET /api/v1/items/{id}` - Détails item

## 🎯 Objectif

Ce projet illustre comment Renovate peut transformer la maintenance d'une application avec plus de 15 dépendances obsolètes en un processus automatisé et sécurisé.

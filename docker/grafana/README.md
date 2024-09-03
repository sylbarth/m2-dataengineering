# Environnement Grafana+Mariadb

# Installation
On se place dans le répertoire courant, puis on exécute:
```sh
docker compose up -d
```

On vérifie que tout fonctionne avec
```sh
docker ps
```

# Base de données (Mariadb)
On se connecte à la base de données sur localhost (port 3306)

# Interface graphique (phpMyAdmin)
On se connecte sur [http://localhost:8080](http://localhost:8080) pour administer les bases de données Mariadb (user: root, pass: master2)

# Interface Grafana
On se connecte sur [http://localhost:3000](http://localhost:3000) (user: admin, pass: admin)

## How to Start?

```
git clone https://github.com/abdulroqib/cmsevents.git
cd cmsevents
docker-compose build
docker-compose up -d
docker-compose exec -T db psql -U postgres -h localhost -d cmsevents < backup.sql
```

### Admin page

http://localhost:8000/admin
username: admin
password: adminadmin
from locust import HttpUser, task


# La classeHttpUserest une instance deHttpSessionqui fournit un client de test.
# Comme pour les tests unitaires, le client permettra de faire la requête sur l’URL de votre choix.
class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task(2)
    def profiles(self):
        self.client.get("/profiles")

    @task(3)
    def lettings(self):
        self.client.get("/lettings")

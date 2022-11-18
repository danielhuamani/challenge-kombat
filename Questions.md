
## Questions

1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. 
De ser posible, que quede solo un commit con los cambios. 

 - Antes de push: git commit --amend
 - Despues de push: git rebase -i HEAD~2, se cambia de pick a squash el primer commit por orden de tiempo 


2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado? 


 He trabajado con dos flujos:
 - git pull, git merge, git push
 - git pull, git merge, git rebase (para unificar tener pocos commits y facilitar el merge)


3.¿Cuál ha sido la situación más compleja que has tenido con esto? 

  un cambio en la logica de negocio, como consecuencia trajo cambio en las tablas y estructura de codigo, asi que se tuvo que hacer migraciones de data y versionamiento de api.


4. ¿Qué experiencia has tenido con los microservicios? 


  He trabajado con microservicios mediante serverless, tambien bajo contenedores con flask y fastapi usando auth0 para unificar los tokens de authenticate


5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué? 


  He tenido mayor experiencia con aws y su cli me parece super practico


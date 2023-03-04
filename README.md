# Job Insights

## Sobre o projeto:
- O projeto exige que sejam desenvolvidas soluções de análises de dados reais sobre empregos. Essas soluções serão testadas e incorporadas em um projeto web, porém, para que isso ocorra só é preciso criar funções de filtragem de informações, aceitando os parâmetros especificados e retornando os resultados corretos.

## O que é de minha autoria:
- Os arquivos `src/jobs.py` e `src/insights.py` que filtram os dados, os arquivos `tests/brazilian/test_brazilian_jobs.py`, `tests/counter/test_counter.py`  e `tests/sorting/test_sorting.py` que testam outras partes do projeto, e a função `job` do arquivo `src/routes_and_views.py` que é responsável por gerar a página de cada um dos jobs.

## Tecnologias utilizadas:
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/-Pytest-fff?style=for-the-badge&logo=pytest" />

## Visualizar Projeto:
- Para ver o projeto são necessários: um Sistema Operacional Unix, Python versão >= 3.8.10, Docker, Docker-compose versão >=1.29.2.
- Tendo os requisitos necessários é preciso clonar o projeto e acessar a pasta dele via terminal.  
- Feito isso, basta iniciar o docker com o comando `docker-compose up -d`.
- Depois que o container docker estiver concluído, acesse a url `http://localhost:5000/`.

## Repositório original do projeto:
https://github.com/tryber/sd-019-b-project-job-insights

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos do projeto
    </strong>
  </summary>
 
  ### Requisitos
  *Nome* | *Avaliação*
  --- | :---:
  1 - Implemente a função read | :heavy_check_mark:
  2 - Implemente a função get_unique_job_types | :heavy_check_mark:
  3 - Implemente a função get_unique_industries | :heavy_check_mark:
  4 - Implemente a função get_max_salary | :heavy_check_mark:
  5 - Implemente a função get_min_salary | :heavy_check_mark:
  6 - Implemente a função filter_by_job_type | :heavy_check_mark:
  7 - Implemente a função filter_by_industry | :heavy_check_mark:
  8 - Implemente a função matches_salary_range | :heavy_check_mark:
  9 - Implemente a função filter_by_salary_range | :heavy_check_mark:
  10 - Implemente um teste para a função count_ocurrences | :heavy_check_mark:
  11 - Implemente um teste para a função read_brazilian_file | :heavy_check_mark:
  12 - Implemente um teste para a função sort_by | :heavy_check_mark:
  13.1 - Crie a rota /job recebendo o parâmetro index | :heavy_check_mark:
  13.2 - Crie a view job, recebendo o parâmetro index | :heavy_check_mark:
  13.3 - Implemente view job para que ela retorne status code 200 para jobs válidos | :heavy_check_mark:
  13.4 - Implemente view job de forma a retornar o HTML exato de uma página de job | :heavy_check_mark:
</details>

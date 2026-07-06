# 🛡️ Sentinela Financeira: Auditoria de Transações e Detecção de Riscos

O **Sentinela Financeira** é um projeto de inteligência de dados de ponta a ponta (*end-to-end*) desenvolvido para auditar fluxos de pagamentos, identificar erros operacionais, duplicidades e sinalizar potenciais fraudes em transações financeiras. 

A solução une o poder de processamento do **Python (Pandas)** para a engenharia de dados e cálculo de regras de compliance, com a capacidade visual do **Power BI (DAX)** para a tomada de decisão executiva.

---

## 🚀 Arquitetura do Projeto

1. **Ingestão e Processamento (Python):** Limpeza de dados, padronização de tipos (datas) e cruzamento de regras de negócio.
2. **Motor de Regras (Python):** Criação de um sistema de pontuação (**Score de Fraude**) e classificação de risco baseada em regras de conformidade.
3. **Visualização e Storytelling (Power BI):** Construção de dashboards interativos com indicadores-chave de performance (KPIs) e visões analíticas para auditoria e diretoria.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Python 3.x**
* **Pandas** (Manipulação e análise de dados)
* **Power BI Desktop** (Modelagem de dados e design de dashboards)
* **DAX - Data Analysis Expressions** (Criação de medidas e KPIs dinâmicos)

---

## 📊 Regras de Negócio e Compliance Aplicadas (Python)

O script Python analisa a base histórica de transações e aplica as seguintes penalidades ao **Score de Fraude** (que varia de 0 a 100):

* **Duplicidades:** Identificação de linhas idênticas com o mesmo *Fornecedor*, *Valor* e *Data*.
* **Valores Suspeitos (+25 pontos):** Transações isoladas com valores acima de R$ 50.000.
* **Operações Fora do Expediente (+15 pontos):** Pagamentos processados em finais de semana (Sábado e Domingo).
* **Fornecedores de Alto Risco (+30 pontos):** Fornecedores historicamente sob suspeita.
* **Incompatibilidade de Centro de Custo:** Identificação de notas de logística e transporte (ex: *Mega Transportes*) faturadas incorretamente no centro de custo de *Recursos Humanos (RH)*.

### Classificação de Risco:
Após o cálculo do score, as transações são segmentadas em faixas:
* **0 a 15:** Baixo Risco
* **16 a 35:** Médio Risco
* **36 a 60:** Alto Risco
* **61 a 100:** Risco Crítico

---

## 📈 Estrutura do Dashboard (Power BI)

O painel foi desenhado seguindo as melhores práticas de UX/UI com um visual *Dark Mode* focado em contraste e escaneabilidade:

1. **Página 1 — Dashboard Executivo:** Visão macro com 6 KPIs principais (Total de Transações, Score Médio de Fraude, Transações Críticas, Valores Suspeitos, Duplicados e um **Índice de Conformidade** dinâmico calculado via DAX).
2. **Página 2 — Investigação de Fraudes:** Visão analítica contendo o Top 10 fornecedores de risco por volume acumulado, distribuição percentual por nível de risco e tabela de auditoria detalhada.
3. **Página 3 — Parecer Executivo:** Relatório integrado direto no painel com os Principais Achados, Recomendações de mitigação e Conclusão técnica para os diretores.

---

## 📁 Como Executar o Projeto

1. Clone o repositório:
```bash
   git clone https://github.com/GabCopriva/sentinela-financeira.git
```

2. Instale as dependências:
```bash
   pip install pandas openpyxl
```

3. Execute o script de análise:
```bash
   python analise_sentinela.py
```

4. Abra o arquivo `.pbix` no Power BI Desktop e atualize os dados apontando para o relatório gerado.

---

## 📬 Contato

Desenvolvido por **Gabriel Copriva de Souza Santos**  
https://www.linkedin.com/in/gabrielcopriva/ · contatogabrielcopriva@gmail.com


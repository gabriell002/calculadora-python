hospitala-python

Script em Python para monitoramento de frequência cardíaca (bpm), que classifica leituras em tempo real como Normal, Alerta ou Crítico, e interrompe o monitoramento automaticamente caso detecte um padrão de risco (três leituras críticas consecutivas).

📖 Sobre o projeto

O script simula um monitor de batimentos cardíacos: a cada execução, o usuário informa um valor de bpm, o sistema classifica essa leitura, contabiliza estatísticas gerais e verifica se houve uma sequência perigosa de leituras críticas, encerrando o monitoramento nesse caso.

🗂️ Estrutura de arquivos
hospitala-python-main/
├── calculadora.py     # Script principal de monitoramento
└── README.md            # Este arquivo
🧩 Detalhamento do código (calculadora.py)
Variáveis de controle
python
total_leituras = 0
normal = 0
alerta = 0
critico = 0
criticos_consecutivos = 0
total_leituras: contador geral de leituras realizadas.
normal, alerta, critico: contadores de quantas leituras caíram em cada classificação.
criticos_consecutivos: contador de quantas leituras críticas em sequência ocorreram (zerado sempre que aparece uma leitura Normal, Alerta ou fora do padrão).
Laço principal (while True)

O script roda em loop infinito, pedindo uma nova leitura de bpm a cada iteração, até que a condição de parada seja atingida.

python
bpm = int(input("Digite a frequência cardíaca (bpm): "))
total_leituras += 1
Classificação da leitura
Faixa de bpm	Classificação	Efeito no contador de críticos consecutivos
60 a 100	✅ Normal	Zera a sequência
101 a 120	⚠️ Alerta	Zera a sequência
> 120	🚨 Crítico	Incrementa a sequência
< 60	Valor fora do padrão	Zera a sequência
python
if 60 <= bpm <= 100:
    ...
elif 101 <= bpm <= 120:
    ...
elif bpm > 120:
    ...
else:
    ...
Condição de parada
python
if criticos_consecutivos == 3:
    print("\n Três estados críticos consecutivos detectados!")
    break

Se o paciente registrar três leituras críticas seguidas (bpm > 120 em três medições consecutivas, sem nenhuma leitura normal/alerta entre elas), o script exibe um alerta e encerra o monitoramento com break.

Relatório
python
print("\n===== RELATÓRIO =====")
print("Total de leituras:", total_leituras)
print("Normal:", normal)
print("Alerta:", alerta)
print("Crítico:", critico)

Exibe um resumo com o total de leituras e quantas caíram em cada categoria.

▶️ Como executar

Pré-requisito: Python 3 instalado.

bash
python3 calculadora.py

Exemplo de execução:

Digite a frequência cardíaca (bpm): 75
Classificação: Normal

===== RELATÓRIO =====
Total de leituras: 1
Normal: 1
Alerta: 0
Crítico: 0

Digite a frequência cardíaca (bpm): 130
Classificação: Crítico

===== RELATÓRIO =====
Total de leituras: 2
Normal: 1
Alerta: 0
Crítico: 1
...

Tecnologias utilizadas
Python 3 (apenas biblioteca padrão, sem dependências externas)
🛠️ Tecnologias utilizadas
Python 3 (apenas biblioteca padrão, sem dependências externas)

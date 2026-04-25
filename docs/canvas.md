
# Canvas MVP — FireVision AI

## 1. Problema de Negócio

Ambientes industriais críticos precisam detectar fumaça e fogo rapidamente. A detecção tardia pode gerar riscos humanos, prejuízos materiais, paralisação operacional e falhas de segurança.

## 2. Pergunta Analítica

Dado um frame de imagem ou vídeo capturado em ambiente industrial, existe fumaça ou fogo? Onde está localizado no frame e qual é o nível de confiança da detecção?

## 3. Usuários / Beneficiários

- Operadores industriais
- Equipes de segurança
- Brigada de incêndio
- Equipes de manutenção
- Gestores de planta
- Centros de monitoramento

## 4. Dados Esperados

Dataset de imagens ou vídeos com exemplos de:

- Fumaça
- Fogo
- Fundo / sem ocorrência
- Variações de iluminação
- Reflexos
- Vapor
- Poeira
- Ambientes industriais complexos

Observação: ainda não temos o dataset. Portanto, esta seção será validada quando os dados forem disponibilizados.

## 5. Variável-Alvo

Classe detectada no frame:

- Fumaça
- Fogo
- Sem ocorrência

## 6. Estratégia de IA

Usar visão computacional para detecção de objetos, preferencialmente com YOLO, por ser uma abordagem adequada para detecção rápida com bounding boxes e múltiplas classes.

## 7. Saída Esperada do MVP

- Imagem/frame processado
- Bounding box
- Classe detectada
- Confiança da predição
- Status do alerta
- Registro dos erros e acertos

## 8. Métricas de Avaliação

- Precisão
- Recall
- F1-score
- Falsos positivos
- Falsos negativos
- Tempo de inferência
- Análise qualitativa dos erros

## 9. Impacto Esperado

Apoiar a detecção precoce de fumaça e incêndio, reduzir tempo de resposta e aumentar a segurança em ambientes industriais.

## 10. Limitações do MVP

Este MVP não representa um sistema industrial final. A proposta é demonstrar a viabilidade técnica inicial, dependendo de validação com dataset real, testes em diferentes cenários e calibração dos limiares de confiança.

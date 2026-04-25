# FireVision AI — Detecção Inteligente de Fumaça e Incêndio

## 1. Desafio escolhido

Desafio 2 — Detecção de Fumaça e Incêndio com IA.

## 2. Problema

Ambientes industriais críticos precisam detectar fumaça e fogo de forma rápida, automatizada e confiável. A detecção tardia pode causar riscos à vida, prejuízos materiais e paralisações operacionais.

## 3. Objetivo do MVP

Construir um protótipo capaz de analisar imagens ou frames de vídeo e identificar sinais de fumaça ou fogo, retornando classe, confiança, localização visual e alerta.

## 4. Pergunta analítica

Dado um frame capturado em ambiente industrial, existe fumaça ou fogo? Onde está localizado e qual é o nível de confiança?

## 5. Estratégia de IA

A solução utiliza visão computacional para detecção de objetos. O modelo de referência é YOLO, por sua capacidade de detecção rápida com bounding boxes e suporte a múltiplas classes.

## 6. Classes

- Fumaça
- Fogo
- Sem ocorrência

## 7. Saídas esperadas

- Imagem processada com bounding box
- Classe detectada
- Confiança
- Status do alerta
- Registro dos acertos e erros

## 8. Métricas

- Precisão
- Recall
- F1-score
- Falsos positivos
- Falsos negativos
- Tempo de inferência
- Análise qualitativa dos erros

## 9. Limitações

Este MVP não representa um sistema industrial final. A solução demonstra a viabilidade técnica inicial e precisa de validação adicional com dados reais, ambientes variados e testes controlados antes de uso em produção.

## 10. Impacto esperado

Apoiar a detecção precoce de fumaça e incêndio, reduzir tempo de resposta e aumentar a segurança em ambientes industriais.

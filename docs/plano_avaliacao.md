
# Plano de Avaliação — FireVision AI

## Objetivo

Avaliar se o MVP consegue detectar fumaça e fogo em imagens ou frames de vídeo de forma confiável, explicável e útil para o contexto industrial.

## O que será avaliado

1. O modelo detecta fumaça?
2. O modelo detecta fogo?
3. O modelo evita falsos positivos?
4. O modelo evita falsos negativos?
5. O tempo de inferência é aceitável para um MVP?
6. Em quais situações o modelo falha?

## Métricas Quantitativas

- Precisão
- Recall
- F1-score
- Falsos positivos
- Falsos negativos
- Tempo médio de inferência

## Avaliação Qualitativa

Registrar exemplos em que o modelo:

- acertou fogo;
- acertou fumaça;
- confundiu vapor/reflexo com fumaça;
- não detectou fogo;
- detectou algo com baixa confiança;
- falhou por iluminação, distância ou fundo complexo.

## Tabela de Avaliação

| ID | Arquivo | Classe Real | Classe Prevista | Confiança | Acertou? | Falso Positivo? | Falso Negativo? | Tempo Inferência | Observação |
|---|---|---|---|---|---|---|---|---|---|

## Observação

Sem dataset real, não serão criadas métricas artificiais. As métricas só serão preenchidas após testes com dados reais ou dados fornecidos oficialmente pelo desafio.

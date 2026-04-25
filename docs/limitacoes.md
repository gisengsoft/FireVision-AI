
# Limitações e Riscos

## Limitações Atuais

- Dataset ainda não disponível.
- Modelo ainda não treinado/testado.
- Métricas reais ainda não calculadas.
- Ambiente industrial real ainda não validado.
- MVP não substitui sistema de segurança certificado.

## Riscos Técnicos

- Falsos positivos causados por vapor, poeira, reflexos ou iluminação intensa.
- Falsos negativos em fumaça pequena, fogo distante ou imagem de baixa qualidade.
- Baixa generalização para ambientes diferentes do dataset.
- Latência elevada se o modelo for pesado.

## Mitigações

- Ajustar limiar de confiança.
- Avaliar falsos positivos e falsos negativos separadamente.
- Testar imagens variadas.
- Documentar os casos de falha.
- Propor revisão humana para casos de baixa confiança.

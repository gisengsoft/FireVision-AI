# Arquitetura do MVP — FireVision AI

## Fluxo Geral

Imagem ou vídeo
→ Pré-processamento
→ Modelo de detecção
→ Classe + confiança + bounding box
→ Regra de alerta
→ Interface visual
→ Registro de resultados

## Componentes

### 1. Entrada

O sistema receberá uma imagem ou frame de vídeo.

### 2. Pré-processamento

Etapa responsável por preparar a imagem para inferência.

Possíveis ações:

- redimensionamento;
- normalização;
- validação do formato;
- extração de frames, caso a entrada seja vídeo.

### 3. Modelo de IA

Modelo de detecção de objetos, preferencialmente YOLO.

Saída esperada:

- classe detectada;
- confiança;
- coordenadas da bounding box.

### 4. Regra de Alerta

Regra inicial proposta:

- Sem detecção: Normal
- Fumaça detectada: Atenção
- Fogo detectado: Risco Alto
- Baixa confiança: Revisão Humana

### 5. Interface

Interface simples para demonstrar o MVP:

- upload de imagem;
- botão de análise;
- exibição da imagem processada;
- exibição da classe, confiança e alerta.

## Observação

Enquanto o dataset e o modelo não forem disponibilizados, a arquitetura será preparada sem inventar resultados.

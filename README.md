# Jogo de Adivinhação de Palavras - Termo

Este é um emocionante jogo de adivinhação de palavras inspirado no jogo "Termo" disponível em [https://term.ooo/](https://term.ooo/). Teste suas habilidades enquanto tenta decifrar palavras aleatórias escolhidas pelo sistema. No modo clássico, o usuário dispõe de 6 tentativas para desvendar a palavra secreta. A cada tentativa, o sistema destaca as letras corretas na posição exata com verde e na posição errada, com amarelo, e as letras ausentes na palavra com preto. O jogador vence ao acertar a palavra. Ao acertar a palavra, ela não será sorteada novamente.

Além deste modo, o jogo oferece outras modalidades. No modo dueto, o desafio é adivinhar duas palavras simultaneamente em 7 tentativas, mantendo a lógica do modo clássico. Se o jogador acertar uma das palavras, ela é retirada das tentativas subsequentes. Para vencer, é necessário acertar ambas as palavras. Já no modo quarteto, o desafio amplia-se para quatro palavras, com 9 tentativas para acertar.

## Funcionalidades do Sistema

- **Jogar:** Desvende as palavras usando pistas de cores (verde para letras corretas na posição exata, amarelo para letras corretas na posição errada e preta para letras ausentes). O modo clássico é definido como padrão. Caso deseje jogar outro modo, acesse o menu de opções.

- **Opções:** Acesse opções adicionais para alterar o modo de jogo, redefinir palavras, adicionar novas palavras ao dicionário e remover palavras indesejadas.

- **Modo de jogo:** Altere entre os modos de jogo disponíveis (clássico, dueto e quarteto). O modo clássico é definido como padrão.

- **Redefinir Palavras:** Redefine as palavras acertadas, permitindo que sejam sorteadas novamente.

- **Adicionar palavra:** Adiciona uma nova palavra ao dicionário, caso não exista, e à lista de palavras sorteadas.

- **Remover palavra:** Remove uma palavra indesejada do dicionário e da lista de palavras sorteadas.

## Arquitetura do Sistema

O sistema foi desenvolvido seguindo uma arquitetura modular, com os seguintes módulos:

- **Módulo Word:** Gerencia operações relacionadas às palavras do jogo, como sortear as palavras, verificar se ela existe, adicionar e remover, etc.;

- **Módulo Table:** Lida com a exibição e formatação das tabelas para apresentar as pistas ao jogador.

- **Módulo Termo:** Contém a lógica central do jogo, incluindo a verificação de vitória e o feedback ao jogador.

- **Módulo Menu:** Gerencia os menus e cabeçalhos e permite que o usuário selecione as opções desejadas.

- **Módulo Main:** Responsável por integrar todos os módulos e chamar as funções.

## Arquivos

O sistema possui os seguintes arquivos:

- **Dict5.txt:** Arquivo contendo mais de 10000 palavras de 5 letras. Utilizado para verificar a veracidade da palavra digitada pelo usuário. Foi utilizado o repositório https://github.com/fserb/pt-br/blob/master/README.md para selecionar as palavras.

- **All_words.txt:** Lista de palavras que poderão ser sorteadas pelo sistema. O site https://www.dicio.com.br/palavras-com-cinco-letras/ foi utilizado para criar a lista.

- **Used_words.txt:** Lista contendo as palavras que já foram acertadas pelo usuário e não serão sorteadas novamente.

## Requisitos

Certifique-se de instalar a biblioteca unidecode antes de executar o jogo. Use o seguinte comando no seu terminal:

```bash
pip install Unidecode
```

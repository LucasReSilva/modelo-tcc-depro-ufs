<p align="center">
  <img src="figuras/logo-projeto.svg" alt="Modelo TCC · DEPRO/UFS" width="700">
</p>

# Modelo LaTeX de TCC — DEPRO/UFS (`modelo-tcc-depro-ufs`)

<p align="center">
  <a href="https://github.com/LucasReSilva/modelo-tcc-depro-ufs/actions/workflows/build.yml"><img src="https://github.com/LucasReSilva/modelo-tcc-depro-ufs/actions/workflows/build.yml/badge.svg" alt="Compilar PDF (LaTeX)"></a>
  <a href="https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2FLucasReSilva%2Fmodelo-tcc-depro-ufs%2Farchive%2Frefs%2Fheads%2Fmain.zip&engine=pdflatex&main_document=tcc-depro-ufs.tex"><img src="https://img.shields.io/badge/Overleaf-Abrir%20no%20Overleaf-47A141?logo=overleaf&logoColor=white" alt="Abrir no Overleaf"></a>
  <a href="https://github.com/abntex/abntex2"><img src="https://img.shields.io/badge/LaTeX-abnTeX2-008080?logo=latex&logoColor=white" alt="LaTeX abnTeX2"></a>
  <img src="https://img.shields.io/badge/ABNT-NBR%2014724%20%7C%2010520%20%7C%206023-1D4ED8" alt="Normas ABNT">
  <a href="https://oleafly.com/"><img src="https://img.shields.io/badge/IDE%20local-Oleafly-0F766E?logo=github&logoColor=white" alt="IDE local Oleafly"></a>
  <img src="https://img.shields.io/badge/DEPRO%2FUFS-Engenharia%20de%20Produ%C3%A7%C3%A3o-0A1E52" alt="DEPRO UFS">
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg" alt="Licença MIT"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/PRs-bem--vindos-brightgreen.svg" alt="PRs bem-vindos"></a>
</p>

Modelo não oficial em LaTeX (`abnTeX2`) para Trabalhos de Conclusão de Curso (TCC) do **Departamento de Engenharia de Produção (DEPRO)** da **Universidade Federal de Sergipe (UFS)**, adaptado do modelo institucional `Modelo DEPRO 003 - Trabalho de Conclusao de Curso.docx` e alinhado às normas da ABNT (**NBR 14724**, **NBR 6023**, **NBR 6024**, **NBR 6027**, **NBR 6028** e **NBR 10520**).

## Recursos do modelo

- **Elementos pré-textuais completos:** capa com brasão vetorial da UFS (`logo-ufs.pdf`) e logotipo vetorial do DEPRO (`logo-depro.pdf`, com fonte editável `logo-depro.svg` em `figuras/`), folha de rosto (com coorientador e subtítulo opcionais), folha de aprovação, agradecimentos, resumo, *abstract*, listas separadas de figuras, quadros e tabelas (além de lista de códigos opcional), lista de abreviaturas e siglas, lista de símbolos e sumário (posicionado por último, conforme a NBR 14724).
- **Contagem correta de páginas:** contagem sequencial iniciada na folha de rosto (oculta nos elementos pré-textuais) e numeração visível em algarismos arábicos no canto superior direito a partir da Introdução.
- **Hierarquia de seções ABNT NBR 6024:** seções primárias em caixa alta e negrito (`1 INTRODUÇÃO`), secundárias em inicial maiúscula e negrito (`2.1 Objetivo geral`), terciárias em negrito e itálico, todas em 12 pt.
- **Quadros e Tabelas diferenciados:** ambiente nativo `quadro` (fechado nas quatro laterais, para dados qualitativos, gerando corretamente `Quadro 1 – ...` na Lista de Quadros) separado de `table` (padrão aberto com `booktabs`, para dados numéricos).
- **Códigos-fonte com `listings`:** suporte nativo compatível com `pdfLaTeX`, quebra de página automática, acentos UTF-8 em português, linguagens pré-configuradas (`Python`, `R`, `SQL`, `Matlab`, `VBA`) e lista de códigos opcional.
- **Fluxograma editável em TikZ:** diagrama metodológico em `capitulos/procedimentos-metodologicos.tex` gerado diretamente via código vetorial.
- **Compilação automatizada:** pronto para compilação local com **[Oleafly](https://oleafly.com/)** (recomendado), linha de comando (`latexmk` / `pdflatex` + `bibtex`), uso online no **Overleaf** (com abertura direta em 1 clique) e verificação contínua via GitHub Actions.

## Estrutura do projeto

```text
modelo-tcc-depro-ufs/
├── tcc-depro-ufs.tex            # Arquivo principal (preâmbulo e estrutura)
├── referencias.bib              # Base bibliográfica (BibTeX / abntex2cite)
├── codigos/                     # Arquivos de código-fonte externos importados via listings
├── dados/                       # Arquivos CSV externos para tabelas (csvsimple)
├── figuras/                     # Logotipos vetoriais (logo-ufs.pdf, logo-depro.pdf, logo-depro.svg) e imagens
├── pre-textuais/                # Capa, folhas iniciais, resumos, listas e sumário
├── capitulos/                   # Seções textuais do trabalho
├── pos-textuais/                # Referências, apêndices e anexos
├── .latexmkrc                   # Configuração do latexmk
├── Makefile                     # Atalhos de compilação e limpeza
├── .github/workflows/build.yml  # Compilação automática no GitHub Actions
├── CHANGELOG.md                 # Histórico de versões do modelo
├── CITATION.cff                 # Metadados de citação acadêmica (CFF 1.2.0)
├── CODE_OF_CONDUCT.md           # Código de conduta da comunidade
├── CONTRIBUTING.md              # Guia de contribuição e validação
├── LICENSE                      # Licença MIT do código-fonte LaTeX
├── SECURITY.md                  # Política de segurança e relato de vulnerabilidades
└── THIRD_PARTY_LICENSES.md      # Licenças de pacotes LaTeX, CI e ativos institucionais
```

## Como usar

### Opção 1: Compilação local com Oleafly (recomendado)

Para editar e compilar localmente sem depender da nuvem, recomenda-se o **[Oleafly](https://oleafly.com/)** ([repositório oficial](https://github.com/Oleafly/Oleafly)) — uma IDE LaTeX de código aberto para Windows, macOS e Linux, com visualização em tempo real e SyncTeX.

#### Como abrir este projeto no Oleafly

Você pode abrir o modelo no Oleafly de três formas:

1. **Via arquivo `.zip` (sem precisar usar Git):**
   - Baixe o repositório no GitHub em **Code > Download ZIP** (ou baixe o código-fonte da [última release](https://github.com/LucasReSilva/modelo-tcc-depro-ufs/releases/latest)).
   - No Oleafly, acesse **New project → Import a project → Existing project (`.zip`)** e selecione o arquivo baixado.
2. **Via `git clone` e pasta local (ou CLI do Oleafly):**
   ```sh
   git clone https://github.com/LucasReSilva/modelo-tcc-depro-ufs.git
   oleafly open modelo-tcc-depro-ufs
   ```
   *(Se preferir usar apenas a interface gráfica, clique em **Open folder…** na biblioteca inicial do Oleafly e selecione a pasta `modelo-tcc-depro-ufs`.)*
3. **Via integração com o GitHub:**
   - Conecte sua conta em **Settings → Integrations → GitHub**.
   - Acesse **New project → Import a project → GitHub** e selecione este repositório.

#### Configuração e edição no Oleafly

1. **Motor de compilação (`pdfLaTeX` / `latexmk`):** ao importar um projeto, o Oleafly usa o compilador **Tectonic** por padrão, a menos que **Settings → Engines → LaTeX** esteja configurado para **`latexmk`**. Como este modelo depende de `abntex2`/`abntex2cite` e foi validado com **`pdfLaTeX`**, certifique-se de ter uma distribuição LaTeX instalada (TeX Live, MiKTeX ou TinyTeX, com os pacotes `abntex2`, `abntex2cite`, `babel`, `mathptmx`, `tikz`, `microtype`, `booktabs`, `tabularx`, `csvsimple`, `listings`, `xcolor`, `amsmath`, `amssymb`, `etoolbox` e `iftex`; além de `hyperxmp`, `xurl` e `pdfpages` opcionais) e configure o motor do projeto para **`latexmk`** / **`pdfLaTeX`** (já configurado via `.latexmkrc`).
2. Defina `tcc-depro-ufs.tex` como documento principal.
3. Edite seus dados pessoais no preâmbulo de `tcc-depro-ufs.tex` (`\nomealuno`, `\titulotrabalho`, `\nomeorientador`, `\nomecoorientador`, etc.).
4. Escreva o conteúdo nas pastas `pre-textuais/`, `capitulos/` e `pos-textuais/` e adicione suas fontes em `referencias.bib`.
5. Antes da entrega final, substitua ou remova o anexo de instruções em `pos-textuais/anexos.tex`.

> **Nota (`pdfLaTeX` e Windows com MiKTeX):** **`pdfLaTeX`** é o motor compilador validado do modelo. No Windows com **MiKTeX**, o comando `latexmk` exige o **Strawberry Perl** instalado; caso não o tenha instalado, utilize a sequência `pdflatex` + `bibtex` (Opção 2) ou selecione diretamente o compilador `pdfLaTeX`.

### Opção 2: Compilação local via linha de comando

Com TeX Live ou MiKTeX instalados, compile diretamente pelo terminal usando **`pdfLaTeX`** via `latexmk`:

```sh
latexmk -pdf tcc-depro-ufs.tex
```

Ou manualmente na sequência tradicional (`pdflatex` + `bibtex`, sem necessidade de Perl):

```sh
pdflatex tcc-depro-ufs.tex
bibtex tcc-depro-ufs
pdflatex tcc-depro-ufs.tex
pdflatex tcc-depro-ufs.tex
```

No Linux/macOS/WSL, também é possível usar `make` e `make clean`.

### Opção 3: Compilação online no Overleaf

[![Abrir no Overleaf](https://img.shields.io/badge/Overleaf-Abrir%20%C3%BAltima%20vers%C3%A3o%20da%20main-47A141?logo=overleaf&logoColor=white)](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2FLucasReSilva%2Fmodelo-tcc-depro-ufs%2Farchive%2Frefs%2Fheads%2Fmain.zip&engine=pdflatex&main_document=tcc-depro-ufs.tex)

1. Clique no botão acima ou acesse o **[link direto para abrir a última versão da `main` no Overleaf](https://www.overleaf.com/docs?snip_uri=https%3A%2F%2Fgithub.com%2FLucasReSilva%2Fmodelo-tcc-depro-ufs%2Farchive%2Frefs%2Fheads%2Fmain.zip&engine=pdflatex&main_document=tcc-depro-ufs.tex)** — o Overleaf criará automaticamente uma cópia do repositório já configurada com **`pdfLaTeX`** e **`tcc-depro-ufs.tex`** como arquivo principal. *(Observação: a importação via link cria uma cópia independente no momento da abertura, sem sincronização bidirecional automática com o GitHub.)*
2. Como alternativa manual, baixe o repositório como `.zip` (**Code > Download ZIP**) e envie no Overleaf (**New Project > Upload Project**), conferindo em **Menu > Settings**:
   - **Compiler:** `pdfLaTeX`
   - **Main document:** `tcc-depro-ufs.tex`
3. Edite os arquivos e compile normalmente.


## Dicas rápidas de edição

- **Coorientador e subtítulo:** em `tcc-depro-ufs.tex`, se não houver coorientador ou subtítulo, basta deixar `\newcommand{\nomecoorientador}{}` e `\newcommand{\subtitulotrabalho}{}` vazios (`{}`).
- **Dedicatória e epígrafe opcionais:** os arquivos `pre-textuais/dedicatoria.tex` e `pre-textuais/epigrafe.tex` já existem prontos no projeto; basta descomentar as linhas correspondentes em `tcc-depro-ufs.tex` para utilizá-los.
- **Ficha catalográfica (BICEN/UFS):** para o depósito final, solicite a ficha catalográfica em PDF à biblioteca e insira-a após a folha de rosto descomentando `\includepdf` em `tcc-depro-ufs.tex` (requer o pacote `pdfpages`).
- **Quadros vs. Tabelas:** use `\begin{quadro} ... \end{quadro}` para informações textuais/qualitativas e `\begin{table} ... \end{table}` para dados numéricos. Em ambos, utilize `\caption{...}`, `\label{...}` e `\fonte{...}`.
- **Tabelas a partir de CSV:** use `\csvreader` (pacote `csvsimple`), conforme exemplificado em `capitulos/resultados-e-discussao.tex`. O arquivo CSV em `dados/` já deve estar formatado e pronto para exibição (casas decimais, separador `;` e eventuais totais).
- **CSV no Excel:** ao exportar planilhas em português no Excel, salve como **CSV UTF-8** (com separador `;` e a primeira linha reservada ao cabeçalho).
- **Códigos-fonte (`listings`):** use `\begin{lstlisting} ... \end{lstlisting}` para código inline ou `\lstinputlisting{codigos/...}` para importar arquivos separados (como exemplificado em `pos-textuais/anexos.tex` com `codigos/exemplo-eficiencia.py`), com compatibilidade `pdfLaTeX`, quebra de página automática, acentos UTF-8 em português e linguagens prontas (`Python`, `R`, `SQL`, `Matlab` e `VBA`). Indique a origem do trecho com `\fontecodigo{...}`; caso não utilize códigos-fonte no trabalho final, lembre-se de comentar `pre-textuais/lista-de-codigos.tex` em `tcc-depro-ufs.tex`.
- **Citações ABNT:** use `\cite{chave}` para citações entre parênteses e `\citeonline{chave}` para citações integradas ao texto.
- **Anexo de instruções e listas opcionais:** antes da entrega final, lembre-se de comentar ou substituir `pos-textuais/anexos.tex` e de comentar em `tcc-depro-ufs.tex` as listas opcionais não utilizadas (figuras, quadros, tabelas, códigos, siglas ou símbolos).

## Diferenças e justificativas em relação ao modelo DOCX

O arquivo institucional de origem (`Modelo DEPRO 003 - Trabalho de Conclusao de Curso.docx`, datado de 2021) serviu como base estrutural e visual. Na adaptação para LaTeX, foram realizadas correções normativas e melhorias técnicas detalhadas abaixo:

| Elemento / Aspecto | Modelo DOCX original (2021) | Modelo LaTeX (`modelo-tcc-depro-ufs`) | Justificativa técnica / normativa |
| :--- | :--- | :--- | :--- |
| **Posição do Sumário** | Aparecia **antes** das listas de figuras, quadros, tabelas, siglas e símbolos (`p. vi`). | Posicionado como **último elemento pré-textual** (após todas as listas). | A **ABNT NBR 14724 (seção 4.2.1)** determina que o sumário deve ser o último elemento pré-textual, sucedendo todas as listas opcionais. |
| **Numeração das páginas pré-textuais** | Exibia algarismos romanos minúsculos no rodapé (`ii` a `xi`), iniciando a parte textual em `12`. | Contagem sequencial oculta a partir da folha de rosto, exibindo arábicos (`12`, `13`, ...) apenas a partir da Introdução. | A **ABNT NBR 14724 (seção 5.3)** estabelece que todas as folhas a partir da folha de rosto são contadas, mas **não numeradas**; a numeração impressa inicia na parte textual, no canto superior direito. |
| **Cabeçalho na Folha de Rosto** | Repetia os logotipos UFS/DEPRO da capa na folha de rosto e centralizava `Orientador`/`Coorientador` fora do bloco recuado. | Folha de rosto limpa (sem cabeçalho de logotipos) e orientação integrada ao bloco recuado à direita. | Atende à **ABNT NBR 14724 (seção 4.2.1.1.2)**, que reserva a identificação institucional completa à capa e mantém natureza do trabalho + orientação alinhados do centro para a margem direita. |
| **Nomenclatura de listas e referências** | Usava `REFERÊNCIAS BIBLIOGRÁFICAS` e `LISTA DE SIGLAS`. | Adota `REFERÊNCIAS` e `LISTA DE ABREVIATURAS E SIGLAS`. | Nomenclatura oficial da **ABNT NBR 14724** e **NBR 6023** (referências incluem fontes não bibliográficas, como normas, sites e softwares). |
| **Ordem da Lista de Siglas** | Listava `ABNT`, `NBR`, `TCC`, `FMEA` fora da ordem alfabética. | Ordenada alfabeticamente (`ABNT`, `FMEA`, `NBR`, `TCC`), com termo estrangeiro em itálico. | A **ABNT NBR 14724 (seção 4.2.1.6)** exige ordem alfabética rigorosa na lista de abreviaturas e siglas. |
| **Equação de exemplo e símbolos** | Apresentava $A = 2\pi R^2$ para área do círculo e símbolo $R$ na lista, em vez de $r$. | Corrige a fórmula para $A = \pi r^2$ e unifica $A$ e $r$ entre Capítulo 1 e Lista de Símbolos, preservando numeração contínua `(1)` e bloco `em que:`. | Corrige erro matemático do exemplo original mantendo total consistência simbólica e formatação ABNT. |
| **Roteiro de trabalho (`Figura 2`)** | Diagrama criado como *SmartArt* editável no Word. | Desenhado nativamente em **TikZ** (`capitulos/procedimentos-metodologicos.tex`). | Mantém a mesma editabilidade direta em texto que o *SmartArt* proporcionava no Word, com qualidade vetorial nativa no PDF e sem depender de imagens externas. |
| **Objetivos específicos** | Lista alfabética simples (`a)`, `b)`, `c)`) sem pontuação final nas alíneas. | Usa o ambiente `alineas` do `abnTeX2`, com ponto e vírgula nos itens e ponto final no último. | Segue as regras de alíneas da **ABNT NBR 6024:2012 (seção 4.2)**. |
| **Quadros vs. Tabelas** | Estilos *Word* separados (`Modelo Quadro DEPRO` fechado e `Modelo Tabela DEPRO` aberto). | Ambiente nativo `quadro` (fechado nos quatro lados, cabeçalho sombreado e `Lista de quadros` própria) separado de `table` (`booktabs`, laterais abertas). | Preserva a diferenciação visual do modelo DEPRO em conformidade com as normas do **IBGE** (tabelas abertas para dados numéricos; quadros fechados para dados textuais/qualitativos). |
| **Seções e subseções** | Primárias em caixa alta e negrito; secundárias em inicial maiúscula e negrito. | Mantém `chapter=TITLE` (`12 pt`, caixa alta, negrito) e hierarquia progressiva em `12 pt` até 4 níveis sem caixa alta em `\section`. | Garante fidelidade ao DOCX e aderência à **ABNT NBR 6024:2012**. |
| **Anexo de instruções (`Anexo A`)** | Contava com instruções e capturas de tela do Microsoft Word. | Substituído por guia prático para LaTeX/[Oleafly](https://github.com/Oleafly/Oleafly) em `pos-textuais/anexos.tex` (com aviso para remoção antes da entrega). | Adapta as orientações de uso para o ecossistema LaTeX sem carregar capturas de tela obsoletas do Word. |
| **Recursos extras de produtividade e metadados** | Uso exclusivamente manual no Word e logotipos rasterizados. | Campos condicionais (`\nomecoorientador`, `\subtitulotrabalho`), importação de tabelas via **CSV** (`csvsimple`), suporte a códigos-fonte com `listings` (UTF-8 + `Lista de códigos` opcional), logotipos vetoriais em `figuras/` (`logo-ufs.pdf`, `logo-depro.pdf` e `logo-depro.svg`), `microtype`, metadados básicos de acessibilidade no PDF (`pdflang`, `DisplayDocTitle`, `alt={...}`, `glyphtounicode`, `hyperxmp` opcional e marcadores) e CI no GitHub Actions. | Reduz erros de formatação manual, facilita atualização de dados tabulares e listagens de código, garante qualidade vetorial aos logotipos em qualquer escala, aprimora metadados/navegação do PDF (sem equivaler a PDF/UA com *tagging* estrutural completo) e automatiza a geração do PDF final. |

## Observação normativa

- **Diretrizes institucionais:** embora este modelo incorpore correções estruturais alinhadas à **ABNT NBR 14724** e às demais normas aplicáveis, confirme sempre eventuais diretrizes específicas vigentes do DEPRO e do Sistema de Bibliotecas da UFS (BICEN) antes do depósito final.
- **Citações e referências (`abntex2cite`):** a bibliografia utiliza `abntex2cite` (padrão BibTeX autor-data em caixa alta entre parênteses, adotado pela praticidade e compatibilidade imediata com `pdfLaTeX`). Caso a banca ou a BICEN exijam estritamente a grafia `(Sobrenome, ano)` introduzida pela **ABNT NBR 10520:2023**, recomenda-se migrar a gestão bibliográfica para `biblatex-abnt` + `biber`.
- **Acessibilidade no PDF:** os recursos aplicados cobrem metadados básicos e navegação (`pdflang`, `DisplayDocTitle`, `alt={...}`, `glyphtounicode`, `hyperxmp` opcional e marcadores), **sem equivaler a conformidade PDF/UA com *tagging* estrutural completo**, devido a limitações atuais do conjunto `abnTeX2`/`memoir`.

## Como citar, comunidade e licenças

- **Como citar:** caso utilize ou adapte este modelo em seu trabalho acadêmico ou pesquisa, consulte os metadados de citação em [`CITATION.cff`](CITATION.cff) (ou utilize o botão **Cite this repository** no GitHub).
- **Histórico de alterações:** veja [`CHANGELOG.md`](CHANGELOG.md).
- **Contribuições e conduta:** consulte [`CONTRIBUTING.md`](CONTRIBUTING.md) e o [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
- **Segurança:** para relatar vulnerabilidades, siga as orientações em [`SECURITY.md`](SECURITY.md).
- **Licença:** o código LaTeX e os scripts de automação deste repositório são distribuídos sob a licença MIT (consulte [`LICENSE`](LICENSE)). Os logotipos da UFS e do DEPRO em `figuras/` pertencem às respectivas instituições e são mantidos apenas para identificação acadêmica nos trabalhos do curso; detalhes adicionais sobre pacotes LaTeX e dependências de terceiros constam em [`THIRD_PARTY_LICENSES.md`](THIRD_PARTY_LICENSES.md).


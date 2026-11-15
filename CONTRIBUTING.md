# Como contribuir

Obrigado pelo interesse em melhorar o `modelo-tcc-depro-ufs`! Este guia explica como configurar um ambiente local de compilação, verificar alterações nas normas da ABNT ou do DEPRO/UFS e enviar contribuições com qualidade.

Antes de iniciar mudanças extensas, abra uma *issue* para alinharmos a abordagem normativa ou técnica.

## Formas de contribuir

- **Relatar um erro:** abra uma [issue](https://github.com/LucasReSilva/modelo-tcc-depro-ufs/issues/new) descrevendo o problema, a página/seção afetada e o erro de compilação ou desvio normativo.
- **Sugerir melhorias:** proponha novas funcionalidades, atualizações da ABNT ou ajustes institucionais do DEPRO/BICEN em uma *issue*.
- **Reportar uma vulnerabilidade:** por favor, não abra uma *issue* pública; consulte [`SECURITY.md`](SECURITY.md).
- **Enviar um *Pull Request*:** siga o fluxo descrito abaixo.

## Pré-requisitos

| Ferramenta | Versão / Observação | Notas |
| --- | --- | --- |
| Distribuição LaTeX | [TeX Live](https://www.tug.org/texlive/), [MiKTeX](https://miktex.org/) ou [TinyTeX](https://yihui.org/tinytex/) | Deve incluir `pdflatex`, `bibtex` e os pacotes `abntex2`, `abntex2cite`, `babel`, `mathptmx`, `tikz`, `microtype`, `booktabs`, `tabularx`, `csvsimple`, `listings`, `xcolor`, `amsmath`, `amssymb`, `etoolbox` e `iftex` (`hyperxmp`, `xurl` e `pdfpages` opcionais). |
| `latexmk` | Incluído no TeX Live / MiKTeX | No Windows com MiKTeX, exige **Strawberry Perl** instalado; caso contrário, use `pdflatex` + `bibtex`. |
| [Oleafly](https://oleafly.com/) *(opcional)* | Última versão estável | IDE local recomendada; permite compilar com `latexmk` e validar o projeto via `oleafly check`. |
| [Git](https://git-scm.com/) | Qualquer versão recente | Controle de versão e envio de *Pull Requests*. |
| GNU `make` *(opcional)* | Linux / macOS / WSL | Atalhos definidos em [`Makefile`](Makefile). |

## Primeiros passos

```sh
git clone https://github.com/LucasReSilva/modelo-tcc-depro-ufs.git
cd modelo-tcc-depro-ufs

# Compilação recomendada (usa .latexmkrc com pdfLaTeX + BibTeX):
latexmk -pdf tcc-depro-ufs.tex
```

Se preferir compilar manualmente sem `latexmk` (ou sem Perl no Windows):

```sh
pdflatex -interaction=nonstopmode tcc-depro-ufs.tex
bibtex tcc-depro-ufs
pdflatex -interaction=nonstopmode tcc-depro-ufs.tex
pdflatex -interaction=nonstopmode tcc-depro-ufs.tex
```

Para abrir diretamente no Oleafly a partir do terminal:

```sh
oleafly open .
```

## Estrutura do projeto

```text
tcc-depro-ufs.tex            # Preâmbulo ABNT, macros do DEPRO e documento mestre
referencias.bib              # Base bibliográfica BibTeX (abntex2cite)
codigos/                     # Códigos-fonte externos importados nos capítulos, apêndices ou anexos via listings
dados/                       # Planilhas CSV de exemplo importadas via csvsimple
figuras/                     # Logotipos vetoriais institucionais e identidade visual
pre-textuais/                # Capa, folha de rosto, aprovação, resumos, listas e sumário
capitulos/                   # Seções textuais e exemplos (equações, figuras, quadros, tabelas, códigos)
pos-textuais/                # Referências, apêndices e anexo de instruções
.latexmkrc                   # Configuração padrão do latexmk (pdfLaTeX + BibTeX + SyncTeX)
Makefile                     # Atalhos de compilação e limpeza (all, manual, clean, distclean)
.github/workflows/build.yml  # Pipeline de compilação automática no GitHub Actions
```

## Verificações antes de enviar

Toda alteração em arquivos `.tex`, `.bib`, `.csv` ou scripts de build deve ser validada compilando `tcc-depro-ufs.tex` do zero (após `latexmk -C` ou `make distclean`) e conferindo:

1. **Compilação limpa em `pdfLaTeX` sem `--shell-escape`:** o modelo deve compilar sem erros fatais no CI (`.github/workflows/build.yml`) e no Overleaf.
2. **Sumário e listas:** verificar se o sumário aparece após todas as listas opcionais (figuras, quadros, tabelas, códigos, siglas e símbolos) e se a numeração de entradas e páginas bate com o PDF final.
3. **Paginação ABNT:** confirmar contagem sequencial oculta a partir da folha de rosto e numeração arábica visível no canto superior direito a partir da Introdução.
4. **Citações e referências:** assegurar que `bibtex tcc-depro-ufs` executa sem chaves indefinidas (`Citation ... undefined`) ou referências quebradas.
5. **Se usar o Oleafly CLI:** opcionalmente execute `oleafly build` e `oleafly check` para inspeção de pré-voo do PDF.

## Padrões de estilo e edição

- **Codificação e fim de linha:** mantenha todos os arquivos de texto em **UTF-8** com quebras de linha **LF** (conforme configurado em [`.gitattributes`](.gitattributes)).
- **Repositório limpo:** nunca versione arquivos auxiliares ou PDFs gerados (`.aux`, `.bbl`, `.blg`, `.log`, `.pdf` na raiz, etc.), respeitando o [`.gitignore`](.gitignore).
- **Fidelidade normativa e institucional:** documente claramente qualquer mudança que afete regras da ABNT (NBR 14724, 6023, 6024, 6027, 6028, 10520) ou diretrizes do DEPRO/BICEN/UFS.
- **Compatibilidade ampla:** evite pacotes experimentais ausentes no TeX Live padrão ou macros que exijam `LuaLaTeX`/`XeLaTeX` obrigatórios ou `--shell-escape`.

## Pull requests

1. Faça um *fork* do repositório e crie uma *branch* a partir da `main` (`git checkout -b fix/descricao-curta` ou `feat/descricao-curta`).
2. Mantenha o escopo focado; correções não relacionadas devem ir em *Pull Requests* separados.
3. Descreva claramente o que foi alterado, a norma ou requisito institucional atendido e como a compilação foi testada.
4. Verifique se o workflow **`Compilar PDF (LaTeX)`** no GitHub Actions concluiu com sucesso.

## Lançamento de versões (mantenedores)

As versões seguem o [Versionamento Semântico](https://semver.org/lang/pt-BR/):

1. Atualize [`CHANGELOG.md`](CHANGELOG.md) movendo os itens de `[Não lançado]` para a nova versão e atualize `version` / `date-released` em [`CITATION.cff`](CITATION.cff).
2. Crie o *commit* e a *tag* anotada (`vX.Y.Z`), publique no GitHub e anexe o `tcc-depro-ufs.pdf` compilado pelo pipeline à Release.

---

Ao contribuir, você concorda que suas contribuições serão disponibilizadas sob a [Licença MIT](LICENSE) do projeto. Todas as interações na comunidade seguem nosso [Código de Conduta](CODE_OF_CONDUCT.md).


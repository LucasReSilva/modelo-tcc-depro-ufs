# Licenças de Terceiros e Ativos Institucionais

O código LaTeX, os arquivos de exemplo e os scripts de automação do `modelo-tcc-depro-ufs` são distribuídos sob a [Licença MIT](LICENSE).

Este documento lista os componentes de terceiros utilizados ou referenciados pelo modelo, bem como os ativos institucionais incluídos para identificação acadêmica.

---

## Classes e pacotes LaTeX (utilizados na compilação)

O modelo não redistribui binários ou pacotes do TeX no repositório; eles são fornecidos pela distribuição LaTeX do usuário (TeX Live, MiKTeX ou TinyTeX) ou pelo ambiente do Overleaf. Os pacotes carregados em [`tcc-depro-ufs.tex`](tcc-depro-ufs.tex) estão sujeitos às suas respectivas licenças no CTAN:

| Pacote / Classe | Finalidade no modelo | Licença típica (CTAN) |
|---|---|---|
| [`abntex2`](https://www.abntex.net.br/) e `abntex2cite` | Classe base ABNT e citações autor-data (`[alf]`) | LPPL 1.3c |
| [`memoir`](https://ctan.org/pkg/memoir) | Classe subjacente do `abntex2` (layout, listas, sumário e cabeçalhos) | LPPL 1.3c |
| `iftex`, `inputenc`, `fontenc`, `babel` (`brazil`, `english`) | Detecção de motor TeX, codificação UTF-8 e hifenização/rótulos | LPPL 1.3c |
| `mathptmx` | Fonte Times para texto e matemática compatível com o modelo DEPRO | LPPL / GPL (fontes URW) |
| `microtype` | Refinamento tipográfico e protrusão de margens | LPPL 1.3c |
| `graphicx`, `xcolor`, `tikz` (`pgf`) | Inclusão de logotipos vetoriais, cores e fluxograma metodológico | LPPL 1.3c / GPL-2.0 |
| `amsmath`, `amssymb` | Composição de equações e símbolos matemáticos | LPPL 1.3c |
| `booktabs`, `tabularx`, `array` | Formatação profissional de tabelas e quadros | LPPL 1.3c |
| `csvsimple` | Importação automática de tabelas a partir de arquivos CSV (`dados/`) | LPPL 1.3c |
| `listings` | Listagens de código-fonte compatíveis com `pdfLaTeX` (sem `--shell-escape`) | LPPL 1.3c |
| `etoolbox` | Utilitários de programação de macros no preâmbulo | LPPL 1.3c |
| `hyperxmp`, `xurl`, `pdfpages` (opcionais) | Metadados XMP, quebra de URLs longas e inclusão da ficha catalográfica | LPPL 1.3c |

## Automação e Integração Contínua (GitHub Actions)

O fluxo automatizado em [`.github/workflows/build.yml`](.github/workflows/build.yml) utiliza as seguintes ações de código aberto:

| Ação | Finalidade | Licença |
|---|---|---|
| [`actions/checkout`](https://github.com/actions/checkout) | *Checkout* do repositório no runner do GitHub Actions | MIT |
| [`xu-cheng/latex-action`](https://github.com/xu-cheng/latex-action) | Ambiente TeX Live conteinerizado com `latexmk` (`pdfLaTeX`) | MIT |
| [`actions/upload-artifact`](https://github.com/actions/upload-artifact) | Publicação do PDF compilado como artefato da execução | MIT |

## Ativos institucionais (`figuras/`)

Os arquivos de marca abaixo pertencem às respectivas instituições acadêmicas e são mantidos no repositório exclusivamente para identificação institucional nos trabalhos acadêmicos do curso:

| Arquivo | Origem / Titularidade | Condição de uso |
|---|---|---|
| `figuras/logo-ufs.pdf` | Brasão oficial da **Universidade Federal de Sergipe (UFS)** ([ASCOM/UFS](https://ascom.ufs.br/pagina/3217-brasao-e-marcas-da-ufs)) | Uso restrito à identificação institucional acadêmica |
| `figuras/logo-depro.pdf` e `figuras/logo-depro.svg` | Logotipo do **Departamento de Engenharia de Produção (DEPRO/UFS)** | Uso restrito à identificação acadêmica nos trabalhos do departamento |
| `figuras/logo-projeto.svg` | Banner de identificação do projeto `modelo-tcc-depro-ufs` | Distribuído com o projeto sob [Licença MIT](LICENSE), respeitando os direitos dos elementos institucionais acima |

## Documentação e selos

- Os selos (*badges*) exibidos no [`README.md`](README.md) são servidos dinamicamente pelo projeto aberto [Shields.io](https://shields.io/) (CC0 1.0 / MIT).

---

Ao redistribuir este modelo ou trabalhos derivados do código-fonte LaTeX, mantenha o aviso da [Licença MIT](LICENSE) e respeite os termos dos ativos institucionais descritos acima.

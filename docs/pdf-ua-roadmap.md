# Roteiro de acessibilidade PDF/UA

## Situação atual

O ramo `feature/pdf-ua` ativa PDF management e tagging automático com PDF/A-2u e PDF/UA-1. A compilação completa passou no GitHub Actions no commit `c072b63`, após adaptações aos dados de título e ao float `quadro`; o exemplo de código renderizado foi retirado do anexo padrão porque desequilibrava os hooks de parágrafo. Isso comprova que o PDF marcado é gerado, mas não comprova conformidade PDF/UA.

O código atual compilou e foi validado no GitHub Actions (execução [44861187600](https://github.com/LucasReSilva/modelo-tcc-depro-ufs/actions/runs/44861187600)). No relatório veraPDF 1.30.4, a validação PDF/A-2u falhou na regra ISO 19005-2:2011, 6.8, devido a dois arquivos HTML associados (`latex-list-css.html` e `latex-align-css.html`) que não atendem aos requisitos de arquivos embutidos em PDF/A-2. A validação PDF/UA-1 passou 104 regras e falhou em 2 (30 verificações): 26 conteúdos não marcados nas tabelas e 4 elementos `TOC` que contêm parágrafos `P`. Os erros anteriores de hierarquia de títulos, de entradas `TOCI` fora de `TOC` e de contagem de colunas do quadro foram corrigidos. O workflow publica ambos os relatórios como artefatos informativos; uma execução bem-sucedida do workflow não significa que esses relatórios indiquem conformidade.

Avisos anteriores de desequilíbrio dos hooks automáticos de parágrafo foram superados para a compilação completa atual. O projeto Tagged PDF lista `abntex2` e `memoir` como incompatíveis no estado consultado em 2026-11-20, então a árvore estrutural continua exigindo auditoria cuidadosa.

## Bloqueios identificados

- `pdfx` está classificado pelo projeto de marcação do LaTeX como incompatível com o PDF management. O protótipo já o substituiu por `\DocumentMetadata` e removeu o placeholder de `\tagpdfsetup`.
- `abntex2` estende `memoir`; ambos estão classificados como incompatíveis com tagging automático. Embora o documento compile atualmente, a compatibilidade da árvore estrutural ainda não foi comprovada.
- `listings` é parcialmente compatível; o código-fonte e sua lista precisam ser conferidos na árvore de estrutura e na ordem de leitura.
- `tikz` é parcialmente compatível; cada diagrama precisa de texto alternativo significativo. Figuras, tabelas/quadros, matemática, listas, sumário e elementos pré-textuais também precisam de revisão semântica.
- A validação automática cobre requisitos verificáveis por máquina. A ordem de leitura, a utilidade dos textos alternativos e a leitura de fórmulas ainda exigem inspeção humana com tecnologia assistiva.

## Estratégia inicial

Manter PDF/A-2u como requisito do projeto e investigar primeiro PDF/UA-1 (ISO 14289-1), que usa a base PDF 1.7 da ISO 32000-1. A alternativa PDF/UA-2 (ISO 14289-2) oferece suporte mais rico para matemática, mas usa PDF 2.0 e exigiria reavaliar a escolha atual de PDF/A-2u; não será adotada implicitamente.

O protótipo deve usar a implementação atual do LaTeX Tagged PDF, habilitada antes de `\documentclass`, e remover o `pdfx` e o placeholder antes de ativar as chamadas reais de `\tagpdfsetup`. A classe `abntex2` permanece um risco de compatibilidade que precisa ser tratado e comprovado; habilitar o tagging sem essa verificação não é suficiente.

## Próximas etapas

1. Corrigir os quatro elementos `TOC` que ainda contêm filhos `P`; a tentativa de envolver as listas completas foi revertida porque também colocou seus títulos dentro de `TOC`.
2. Marcar corretamente as linhas decorativas das tabelas como artefatos sem envolver o conteúdo textual. A tentativa de marcar os comandos internos do `booktabs` provocou tags aninhadas e foi revertida.
3. Identificar por que o tagging acrescenta os arquivos CSS associados e ajustar sua geração sem remover tags semânticas necessárias; depois, voltar a validar PDF/A-2u.
4. Revisar a árvore estrutural e a ordem de leitura, especialmente elementos pré-textuais, lista de códigos e o fluxograma TikZ; inspecionar com leitor de tela antes de afirmar conformidade PDF/UA.

## Referências técnicas

- [LaTeX Tagged PDF: instruções de uso](https://tagging-project.latex-project.org/documentation/usage-instructions/)
- [Estado de compatibilidade de classes e pacotes com tagging](https://latex3.github.io/tagging-project/tagging-status/)
- [veraPDF: validação PDF/UA e limites dos testes automatizados](https://docs.verapdf.org/validation/)
- [ISO 19005-2:2011 — PDF/A-2](https://www.iso.org/standard/50655.html)
- [ISO 14289-1 — PDF/UA-1](https://www.iso.org/standard/64599.html)
- [ISO 14289-2:2024 — PDF/UA-2](https://www.iso.org/standard/82278.html)

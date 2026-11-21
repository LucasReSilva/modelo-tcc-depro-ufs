# Roteiro de acessibilidade PDF/UA

## Situação atual

O modelo configura PDF/A-2u, idioma e metadados e fornece texto alternativo às marcas institucionais. O fluxograma tem uma descrição em texto adjacente, ainda não associada como alternativa ao objeto gráfico. Esses recursos melhoram extração e navegação, mas não criam uma árvore estrutural marcada para o conteúdo; portanto, não constituem conformidade PDF/UA.

Há também um placeholder em `tcc-depro-ufs.tex`: `\providecommand{\tagpdfsetup}[1]{}`. As configurações de cabeçalho das tabelas que chamam `\tagpdfsetup` são hoje inertes.

## Bloqueios identificados

- `pdfx` está classificado pelo projeto de marcação do LaTeX como incompatível com o PDF management. A declaração de perfil e metadados precisará migrar para `\DocumentMetadata` e interfaces gerenciadas.
- `abntex2` estende `memoir`; ambos estão classificados atualmente como incompatíveis com tagging automático. É necessário testar e adaptar a classe e seus componentes antes de ativar a marcação no documento completo.
- `listings` é parcialmente compatível; o código-fonte e sua lista precisam ser conferidos na árvore de estrutura e na ordem de leitura.
- `tikz` é parcialmente compatível; cada diagrama precisa de texto alternativo significativo. Figuras, tabelas/quadros, matemática, listas, sumário e elementos pré-textuais também precisam de revisão semântica.
- A validação automática cobre requisitos verificáveis por máquina. A ordem de leitura, a utilidade dos textos alternativos e a leitura de fórmulas ainda exigem inspeção humana com tecnologia assistiva.

## Estratégia inicial

Manter PDF/A-2u como requisito do projeto e investigar primeiro PDF/UA-1 (ISO 14289-1), que usa a base PDF 1.7 da ISO 32000-1. A alternativa PDF/UA-2 (ISO 14289-2) oferece suporte mais rico para matemática, mas usa PDF 2.0 e exigiria reavaliar a escolha atual de PDF/A-2u; não será adotada implicitamente.

O protótipo deve usar a implementação atual do LaTeX Tagged PDF, habilitada antes de `\documentclass`, e remover o `pdfx` e o placeholder antes de ativar as chamadas reais de `\tagpdfsetup`. A classe `abntex2` permanece um risco de compatibilidade que precisa ser tratado e comprovado; habilitar o tagging sem essa verificação não é suficiente.

## Etapas de implementação

1. Construir um documento mínimo com `abntex2` e a configuração de metadados/estrutura compatível com PDF/A-2u e PDF/UA-1; verificar a classe, títulos, sumário, tabelas, fórmulas e links.
2. Adaptar os elementos próprios do modelo e remover os comandos-placeholder, preservando a aparência ABNT e a compilação normal sem marcação.
3. Incluir validações informativas no CI para os perfis PDF/A-2u e PDF/UA-1, mantendo a publicação do PDF independente da validação informativa.
4. Revisar o PDF com leitor de tela/visualização da árvore de estrutura, além do veraPDF, antes de afirmar conformidade.

## Referências técnicas

- [LaTeX Tagged PDF: instruções de uso](https://tagging-project.latex-project.org/documentation/usage-instructions/)
- [Estado de compatibilidade de classes e pacotes com tagging](https://latex3.github.io/tagging-project/tagging-status/)
- [veraPDF: validação PDF/UA e limites dos testes automatizados](https://docs.verapdf.org/validation/)
- [ISO 19005-2:2011 — PDF/A-2](https://www.iso.org/standard/50655.html)
- [ISO 14289-1 — PDF/UA-1](https://www.iso.org/standard/64599.html)
- [ISO 14289-2:2024 — PDF/UA-2](https://www.iso.org/standard/82278.html)

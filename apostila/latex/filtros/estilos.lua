-- Prova de conceito: preserva no LaTeX as funções marcadas por estilos do Word.
-- Uso local (fora do Overleaf):
-- pandoc entrada.docx -f docx+styles -t latex \
--   --lua-filter=filtros/estilos.lua --extract-media=imagens -o convertido.tex

local environments = {
  ["Questão central"] = "questaocentral",
  ["Conceito-chave"] = "conceito",
  ["Frase-chave"] = "frasechave",
  ["Exemplo concreto"] = "exemploconcreto",
  ["Atividade"] = "atividade",
  ["Questão"] = "questao",
  ["Resolução comentada"] = "resolucao",
  ["Nota para diagramação"] = "notaeditorial"
}

function Div(element)
  local style = element.attributes["custom-style"]
  local environment = environments[style]
  if not environment then
    return nil
  end

  local output = pandoc.List()
  output:insert(pandoc.RawBlock("latex", "\\begin{" .. environment .. "}"))
  output:extend(element.content)
  output:insert(pandoc.RawBlock("latex", "\\end{" .. environment .. "}"))
  return output
end

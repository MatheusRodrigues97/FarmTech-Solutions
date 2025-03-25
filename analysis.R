# Carregar bibliotecas necessárias
library(readr)
library(dplyr)
library(ggplot2)

# Ler o arquivo CSV
dados_fazenda <- read_csv("dados_fazenda.csv")

# Calcular estatísticas básicas
estatisticas <- dados_fazenda %>%
  group_by(nome) %>%
  summarise(
    media_area = mean(area),
    desvio_padrao_area = sd(area),
    media_linhas = mean(linhas),
    media_dosagem = mean(dosagem_por_metro),
    media_total_produto = mean(total_produto)
  )

# Imprimir estatísticas
print("=== Análise Estatística por Cultura ===")
print(estatisticas)

# Criar visualizações
# Distribuição da área
ggplot(dados_fazenda, aes(x = nome, y = area, fill = nome)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Distribuição da Área por Cultura",
       x = "Tipo de Cultura",
       y = "Área (m²)")

# Uso de produto
ggplot(dados_fazenda, aes(x = nome, y = total_produto, fill = nome)) +
  geom_bar(stat = "identity") +
  theme_minimal() +
  labs(title = "Uso Total de Produto por Cultura",
       x = "Tipo de Cultura",
       y = "Total de Produto (mL)")

# Salvar gráficos
ggsave("distribuicao_area.png")
ggsave("uso_produto.png")
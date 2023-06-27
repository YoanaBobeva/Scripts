BiocManager::install("clusterProfiler")
BiocManager::install("pathview")
BiocManager::install("enrichplot")
library(clusterProfiler)
library(enrichplot)
# we use ggplot2 to add x axis labels (ex: ridgeplot)
library(ggplot2)

# SET THE DESIRED ORGANISM HERE
organism = "org.Hs.eg.db"
BiocManager::install(organism, character.only = TRUE)
library(organism, character.only = TRUE)

# reading in data
df = read.csv("C:\\Users\\Client\\OneDrive - Queen Mary, University of London\\PhD\\PhD back up\\Programing full\\R\\Datasets\\Enrichment table.csv", header=TRUE)

# we want the log2 fold change 
original_gene_list <- df$Log2FC

# name the vector
names(original_gene_list) <- df$UNIPROT.ID

# omit any NA values 
gene_list<-na.omit(original_gene_list)

# sort the list in decreasing order (required for clusterProfiler)
gene_list = sort(gene_list, decreasing = TRUE)

keytypes(org.Dm.eg.db)

gse <- gseGO(geneList=gene_list, 
             ont ="ALL", 
             keyType = "UNIPROT", 
             nPerm = 10000, 
             minGSSize = 3, 
             maxGSSize = 800, 
             pvalueCutoff = 0.05, 
             verbose = TRUE, 
             OrgDb = organism, 
             pAdjustMethod = "none")




require(DOSE)
dotplot(gse, showCategory=10, split=".sign") + facet_grid(.~.sign)


emapplot(gse, showCategory = 10)


ridgeplot(gse) + labs(x = "enrichment distribution")




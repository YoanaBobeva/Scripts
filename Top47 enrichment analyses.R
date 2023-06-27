library(clusterProfiler)
library(enrichplot)
# we use ggplot2 to add x axis labels (ex: ridgeplot)
library(ggplot2)

organism = "org.Hs.eg.db"
BiocManager::install(organism, character.only = TRUE)
library(organism, character.only = TRUE)

tf = read.csv("C:\\Users\\Client\\OneDrive - Queen Mary, University of London\\PhD\\PhD back up\\Programing full\\R\\Datasets\\Top 40 Uniprot.csv", header=TRUE)

# we want the log2 fold change 
gene_list <- tf$Log2FC

# name the vector
names(gene_list) <- tf$UNIPROT.ID

# omit any NA values 
gene2_list<-na.omit(gene_list)

# sort the list in decreasing order (required for clusterProfiler)
gene2_list = sort(gene2_list, decreasing = TRUE)

keytypes(org.Dm.eg.db)

gse <- gseGO(geneList=gene2_list, 
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



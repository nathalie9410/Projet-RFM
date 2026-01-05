# -*- coding: utf-8 -*-
"""
Created on Sat novembre 12 10:24:21 2022

"""
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import squarify
import matplotlib.dates as mdates
import zipfile
import io
import textwrap




st.write("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Lora&display=swap");
html, body, [class*="css"]  {
   font-family: 'Lora', serif;
}
</style>
""", unsafe_allow_html=True)

sns.set_theme()
colors =['#0173b2', '#de8f05', '#029e73', '#d55e00', '#8172b3', '#ca9161', '#c44e52', '#949494', '#ece133', '#56b4e9']

sns.set_palette(sns.color_palette(colors))
c =sns.color_palette(colors)

st.sidebar.title("Sommaire")

pages =["Introduction", "Méthode", "Préconisations", "Conclusion"]
page = st.sidebar.radio("aller vers", pages)


# PAGE INTRODUCTION
if page == pages[0]:
   # "background-image:url(images/background-h1-city.jpg)"
   # TITRE
   st.markdown("<h1 style='text-align: center; font-family:cursive ;color: #dc5534;font-size: 180px;text-shadow: -1px -1px #dc5534, 1px 1px #a00, -3px 0 4px #dc5534;'>RFM</h1>", unsafe_allow_html=True)
   st.markdown("<h1 style='text-align: center; font-family:cursive ;color: #dc5534;font-size: 20px;'>(Recency, Frequency,Monetary)</h1>", unsafe_allow_html=True)
   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown(" <br>", unsafe_allow_html=True)
   st.image("logo_rfm2.png")
   st.markdown(" <br><br><br><br><br><br><br>", unsafe_allow_html=True)
   
   st.markdown("<h2 style='font-weight:lighter; text-align: center; font-size: 60px;text-shadow: -1px -1px #000, 1px 1px #000, -3px 0 4px #000;'>Preprocessing</h2>", unsafe_allow_html=True)
   
   st.title("")
  
   st.markdown("<p style = 'font-size : 22px'>DataFrame Originel <a href =https://www.kaggle.com/zusmani/pakistans-largest-ecommerce-dataset>RFM</a></p>",unsafe_allow_html=True)
   
   # url = "https://drive.google.com/uc?export=download&id=1gWKM0KgTq_PxFYQpMtB78EHmwszOdses"
   # df1 = pd.read_csv(url)


#   # Chemin vers le zip dans ton repo
 #  zip_path = "datasets.zip"
  # csv_name = "Pakistan Largest Ecommerce Dataset.csv"
#
 #  with zipfile.ZipFile(zip_path) as z:
  #    with z.open(csv_name) as f:
   #      df1 = pd.read_csv(
    #        f,
     #       low_memory=False,
      #      na_values=[' ', '\\N', 'NaN ']
       #  )

   # Chemin vers le zip dans le repo
   zip_path = "datasets.zip"

   with zipfile.ZipFile(zip_path) as z:
      # On récupère automatiquement le nom du fichier .csv dans le zip
      csv_files = [name for name in z.namelist() if name.lower().endswith(".csv")]
      st.write("Fichiers trouvés dans le zip :", csv_files)  # debug, optionnel
      # On prend le premier .csv trouvé
      csv_name = csv_files[0]
      with z.open(csv_name) as f:
         df1 = pd.read_csv(
            f,
            low_memory=False,
            na_values=[' ', '\\N', 'NaN ']
         )

   
   #df1= pd.read_csv("Pakistan Largest Ecommerce Dataset.csv")

   st.dataframe(df1.head())
   st.markdown(" <br>", unsafe_allow_html=True)
    
   st.markdown("<p style = 'font-size : 22px'>DataFrame Nettoyé</p>",unsafe_allow_html=True)
   df= pd.read_csv("preprocessing.csv")
   hide_dataframe_row_index = """
         <style>
         .row_heading.level0 {display:none}
         .blank {display:none}
         </style>
         """
   st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)
   st.dataframe(df.head())
   st.markdown(" <br><br>", unsafe_allow_html=True)
    
    

   st.markdown("<h2 style='font-weight:lighter; text-align: center; font-size: 60px;text-shadow: -1px -1px #000, 1px 1px #000, -3px 0 4px #000;'>Story Telling</h2>", unsafe_allow_html=True)
   st.title("")

   # -----------------------------------------------------------------
   # Matrice de corrélation entre les différentes variables numériques
   # -----------------------------------------------------------------
   
   st.markdown("<h4 style='text-align: center;'>Analyse de la relation entre les différentes variables numériques</h4>", unsafe_allow_html=True)
   #fig = plt.figure()
   #sns.heatmap(df.corr(), annot=True, center=0, cmap= "magma", annot_kws={"fontsize":8}, fmt=".2f")
   #st.pyplot(fig);
   fig = plt.figure()
   # On ne garde que les colonnes numériques pour la corrélation
   numeric_df = df.select_dtypes(include="number")
   sns.heatmap(
      numeric_df.corr(),
      annot=True,
      center=0,
      cmap="magma",
      annot_kws={"fontsize": 8},
      fmt=".2f"
   )
   st.pyplot(fig);

   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("""
   ### Ce qu'on observe sur les corrélations
   - Les variables **prix**, **remise** et **revenu net** sont logiquement corrélées entre elles.
   - Les variables **Année** et **Mois** structurent le comportement d'achat mais restent peu corrélées aux montants.
   - Pas de corrélation extrême qui laisserait penser à une variable redondante ou mal construite.
   """)
   #st.markdown(" <br><br>", unsafe_allow_html=True)

   #st.markdown("<p style = 'font-size : 17px;text-align: justify'>Relation de corrélation entre « Net_income_euros » et « Price_euros » uniquement.</p>",unsafe_allow_html=True)
   st.markdown(" <br><br><br><br>", unsafe_allow_html=True)
    
    
   ## évolution de la variable status   
   #st.markdown("<h4 style='text-align: center;'>Évolution du statut des commandes</h4>", unsafe_allow_html=True) 
   #st.markdown(" <br>", unsafe_allow_html=True)    
   
   #annees = df['Year'].unique()
   colors =['#0173b2', '#de8f05', '#029e73', '#d55e00', '#8172b3', '#ca9161', '#c44e52', '#949494', '#ece133', '#56b4e9']
   fig, axes = plt.subplots(2, 3, figsize=(20,14), squeeze=False)

   # -----------------------------------------------------------
   # Évolution du statut des commandes
   # -----------------------------------------------------------
   
   st.markdown(
      "<h4 style='text-align: center;'>Statuts des commandes</h4>",
      unsafe_allow_html=True
   )
   
   annees = df["Year"].unique()

   # palette dédiée : finalisé / annulé / en attente
   #colors_status = ["#0173b2", "#de8f05", "#029e73"]  # bleu / orange / vert
   status_palette = {
      "finalisé": "#0173b2",   # bleu
      "annulé": "#de8f05",     # orange
      "en attente": "#029e73"  # vert
   }
   order_status = ["finalisé", "annulé", "en attente"]

   fig, axes = plt.subplots(2, 3, figsize=(20, 10))

   for i, year in enumerate(annees):
      subset = df[df["Year"] == year]
      # --- Barplot des statuts ---
      ax_bar = axes[0, i]
      sns.countplot(
         data=subset,
         x="Regroupement_status",
         hue="Regroupement_status",
         ax=ax_bar,
         order=order_status,
         dodge=False,
         palette=status_palette
      )
      
      # on supprime la légende (doublon inutile)
      leg = ax_bar.get_legend()
      if leg is not None:
         leg.remove()
      
      ax_bar.set_title(str(year))
      ax_bar.set_xlabel("")
      ax_bar.set_ylabel("Nombre de commandes")
      ax_bar.tick_params(axis="x", rotation=45)

      # on force une échelle en "vrais" nombres de commandes
      #max_count = subset["Regroupement_status"].value_counts().max()
      #ax_bar.set_ylim(0, max_count * 1.10)

      # valeurs au-dessus des barres
      for p in ax_bar.patches:
         height = p.get_height()
         ax_bar.annotate(
            f"{int(height)}",
            (p.get_x() + p.get_width() / 2, height),
            ha="center",
            va="bottom",
            fontsize=8
         )

      # --- Camembert des statuts ---
      ax_pie = axes[1, i]
      counts = (
         subset["Regroupement_status"].value_counts().reindex(["finalisé", "annulé", "en attente"]).dropna()
      )

      ax_pie.pie(
         counts.values,
         labels=counts.index,
         autopct="%1.1f%%",
         startangle=90,
         shadow=True,
         colors=[status_palette[s] for s in counts.index]
      )
         
      ax_pie.set_title(str(year))
      ax_pie.axis("equal")  # cercle bien rond
      
   fig.suptitle(
      "Évolution du statut des commandes",
      fontsize=30,
      color="b",
      y=0.96)
   
   plt.subplots_adjust(
      top=0.88,   # espace entre suptitle et les graphiques
      hspace=0.45 # espace vertical entre barplots et camemberts
   )
   st.pyplot(fig);

   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown(
      "<p style='font-size:17px; text-align: justify'>\
      Evolution négative des commandes finalisées sur la période.<br>\
      Taux moyen d'annulation: 35.63%\
      </p>",
      unsafe_allow_html=True
   )


   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("""
   ### Insights sur le statut des commandes
   - La majorité des commandes sont **finalisées** chaque année.
   - Le **taux d'annulation** augmente progressivement entre 2016 et 2018, ce qui peut traduire soit un durcissement des conditions (fraude, rupture de stock), soit une expérience client à surveiller.
   - Les commandes **en attente** restent marginales, ce qui est plutôt rassurant côté process logistique.

   En pratique, il serait intéressant de :
   - Croiser le statut des commandes avec les **canaux d'acquisition** ou les **moyens de paiement**,
   - Suivre un **taux d'annulation mensuel** pour détecter rapidement les dérives.
   """)
   #st.markdown(" <br><br>", unsafe_allow_html=True)


   
   ## évolution de la variable moyens de paiement    

   st.markdown(" <br><br><br><br>", unsafe_allow_html=True)
        
   #st.markdown("<h4 style='text-align: center;'>Évolution des moyens de paiement</h4>", unsafe_allow_html=True)


   #annees = df['Year'].unique()
    
   #colors = ['#0173b2', '#de8f05', '#029e73', '#d55e00', '#8172b3']

   #labels = ['cod', 'paiement immédiat', 'Paiement en plusieurs fois', 'voucher','portefeuille en ligne']
   #colors1 ={'cod':'#0173b2','paiement immédiat':'#de8f05','Paiement en plusieurs fois':'#029e73','voucher':'#d55e00','portefeuille en ligne':'#8172b3'}
   #fig, axes = plt.subplots(2, 3, figsize=(30,20), squeeze=False)
    
   #for i in range(3):
      #ax = axes[0,i]
      #sns.countplot(df[df['Year']==annees[i]]['Regroupement_payment_method'], palette=colors1, ax=ax)
      #xlabel = ax.get_xticklabels()
      #ylabel = ax.get_yticklabels()
      #plt.setp(xlabel, rotation=45, horizontalalignment='right', fontsize = 20)
      #plt.setp(ylabel,fontsize = 20)
      #ax.set_title(('{}').format(annees[i]), fontsize=30, color='b')
      #ax.set_ylabel("")
      #ax.set_ylim(0,32000)
        
      #for p in ax.patches:
         #ax.annotate('{}'.format(p.get_height()), (p.get_x() + 0.2, p.get_height() + 1))    
   
      #ax = axes[1,i]    
      #ax.pie(df[df['Year']==annees[i]]['Regroupement_payment_method'].value_counts(), 
               #labels=df[df['Year']==annees[i]]['Regroupement_payment_method'].value_counts().index,
               #autopct='%1.1f%%', shadow=True, startangle=90, colors = colors)
   #fig.suptitle('Etat des moyens de paiment', fontsize=40, color='b', y=0.98)
   #plt.tight_layout()
    
   #def make_space_above(axes, topmargin=1):
      #""" increase figure size to make topmargin (in inches) space for 
         #titles, without changing the axes sizes"""
      #fig = axes.flatten()[0].figure
      #s = fig.subplotpars
      #w, h = fig.get_size_inches()
      #figh = h - (1-s.top)*h  + topmargin
      #fig.subplots_adjust(bottom=s.bottom*h/figh, top=1-topmargin/figh)
      #fig.set_figheight(figh)
   #make_space_above(axes, topmargin=2)

   #st.pyplot(fig);



   # -----------------------------------------------------------
   # Évolution des moyens de paiement
   # -----------------------------------------------------------
 
   st.markdown(
      "<h4 style='text-align: center;'>Moyens de paiement</h4>",
      unsafe_allow_html=True
   )
   
   def wrap_label(s, width=16):
      return "\n".join(textwrap.wrap(str(s), width=width))
   
   annees = df["Year"].unique()

   labels_pm = ['cod', 'paiement immédiat', 'Paiement en plusieurs fois', 'voucher','portefeuille en ligne']
   colors_pm = ["#0173b2", "#de8f05", "#029e73", "#d55e00", "#8172b3"]
   palette_pm = dict(zip(labels_pm, colors_pm))

   fig, axes = plt.subplots(2, 3, figsize=(20, 12), squeeze=False)

   for i, year in enumerate(annees):
      subset = df[df["Year"] == year]

      # --- Barplot des moyens de paiement ---
      ax_bar = axes[0, i]
       # on construit une LISTE de couleurs dans le bon ordre
      #pie_colors = [colors1[label] for label in counts_pm.index]
      sns.countplot(
         data=subset,
         x="Regroupement_payment_method",
         hue="Regroupement_payment_method",
         order=labels_pm,
         dodge=False,
         ax=ax_bar,
         palette=palette_pm
      )

      leg = ax_bar.get_legend()
      if leg is not None:
         leg.remove()
      
      ax_bar.set_title(str(year))
      ax_bar.set_xlabel("")
      ax_bar.set_ylabel("Nombre de commandes")
      #ax_bar.tick_params(axis="x", rotation=45)
      ax_bar.set_xticklabels(
         [wrap_label(l, 18) for l in labels_pm],
         rotation=25,
         ha="center"
      )
      ax_bar.margins(y=0.10)

      #max_count = subset["Regroupement_payment_method"].value_counts().max()
      #ax_bar.set_ylim(0, max_count * 1.10)

      # On s'assure qu'il n'y ait PAS de légende sur le barplot
      if ax_bar.get_legend() is not None:
         ax_bar.get_legend().remove()

      # --- Camembert des moyens de paiement ---
      ax_pie = axes[1, i]
      counts_pm = (
         subset["Regroupement_payment_method"]
         .value_counts().reindex(labels_pm)
         .dropna()
      )

      # on construit une LISTE de couleurs dans le bon ordre
      #pie_colors = [colors1[label] for label in counts_pm.index]

      wedges, texts, autotexts = ax_pie.pie(
         counts_pm.values,
         labels=None,
         autopct="%1.1f%%",
         startangle=90,
         shadow=True,
         colors=[palette_pm[m] for m in counts_pm.index],
      )
         
      #ax_pie.pie(
         #counts_pm.values,
         #labels=counts_pm.index,
         #autopct="%1.1f%%",
         #shadow=True,
         #startangle=90,
         #colors=pie_colors
      #)
      
      ax_pie.set_title(str(year))
      ax_pie.axis("equal")

      handles = wedges
      labels = list(counts_pm.index)

   fig.legend(
      handles,
      labels,
      title="Moyen de paiement",
      loc="lower center",
      ncol=5,
      frameon=False,
      bbox_to_anchor=(0.5, 0.02),
      fontsize=15
   )

      #ax_pie.legend(
         #wedges,
         #counts_pm.index,
         #title="Moyen de paiement",
         #loc="center left",
         #bbox_to_anchor=(1.05, 0.5),
         #frameon=False,
         #fontsize=9,
         #title_fontsize=10
      #)
   


   fig.suptitle(
      "Évolution des moyens de paiement",
      fontsize=30,
      color="b",
      y=0.96
   )
   plt.subplots_adjust(
      top=0.88,
      bottom=0.12,
      hspace=0.55,
      wspace=0.30
   )
   #fig.tight_layout(rect=[0, 0, 1, 0.90])
   st.pyplot(fig);

   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("""
   ### Insights sur les moyens de paiement
   - Le **paiement à la livraison (COD)** domine encore, mais sa part diminue au fil des années.
   - Les paiements **en ligne** (portefeuille, carte, paiement en plusieurs fois, voucher) progressent progressivement, signe d'une **maturité digitale** croissante des clients.
   - Les méthodes minoritaires restent stables mais peuvent correspondre à des niches à forte valeur.

   Idées d'actions :
   - Encourager les paiements en ligne via des **remises dédiées** ou la mise en avant de la sécurité.
   - Analyser la **performance par moyen de paiement** (taux d'annulation, panier moyen, fréquence d'achat).
   """)
   
   # -----------------------------------------------------------
   # Évolution du chiffre d'affaires
   # -----------------------------------------------------------
   
   st.markdown(" <br><br><br><br>", unsafe_allow_html=True)
        
   st.markdown("<h4 style='text-align: center;'>Chiffre d'affaires</h4>", unsafe_allow_html=True)

   #######################
   #Rajout d'un ligne de conversion au format datetime
   df['Created_at'] = pd.to_datetime(df['Created_at'])
   ############################
                                     
   mean_sales = df.groupby('Created_at', as_index=False).agg({'Net_income_euros':'mean'})
   median_sales = df.groupby('Created_at', as_index=False).agg({'Net_income_euros':'median'})
          
   ############## Partie originale ################
   #fig, ax=plt.subplots(1,1,figsize = (20,5))
   #plt.plot_date(mean_sales["Created_at"], mean_sales['Net_income_euros'], 
         #xdate=True, 
         #ls='-', label='Moyenne', color =colors[0])
  # plt.plot_date(median_sales["Created_at"], median_sales['Net_income_euros'], 
         #xdate=True, 
         #ls='-', label='Médiane', color =colors[3])
   #plt.legend()
   #fig.suptitle('Évolution de la moyenne et de la médiane du chiffre d\'affaire des ventes', fontsize=30, color='b', y=0.98)
   #plt.tight_layout()
   #ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=(1, 7)))
   #ax.xaxis.set_minor_locator(mdates.MonthLocator())
   #st.pyplot(fig)
   ##################################################

   ############### Partie de remplacement ############
   fig, ax = plt.subplots(figsize=(10, 4))
   ax.plot(
      mean_sales["Created_at"],
      mean_sales["Net_income_euros"],
      linestyle='-',
      marker='o',
      label='Moyenne',
      color=colors[0]
   )

   ax.plot(
      median_sales["Created_at"],
      median_sales["Net_income_euros"],
      linestyle='-',
      marker='o',
      label='Médiane',
      color=colors[3]
   )

   ax.set_xlabel("Date")
   ax.set_ylabel("Chiffre d'affaires (euros)")
   ax.set_title("Évolution de la moyenne et de la médiane du chiffre d'affaires des ventes")
   ax.legend()
   ax.grid(True)
   fig.autofmt_xdate()

   st.pyplot(fig);

   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("""
   ### Lecture de l'évolution du chiffre d'affaires
   - Le chiffre d'affaires est fortement **saisonnier** avec des pics marqués à certaines périodes (lancements produits, soldes, périodes festives…).
   - La **moyenne** et la **médiane** du CA quotidien sont assez éloignées, ce qui indique la présence de **jours “exceptionnels”** qui tirent la moyenne vers le haut.
   - Pour piloter le business, la médiane est souvent plus représentative du **“niveau normal”** d'activité, tandis que la moyenne permet de mesurer l'impact des gros événements.

   Pistes d'analyse complémentaires :
   - Isoler les périodes de **forte activité** et regarder quels produits / catégories les tirent.
   - Suivre le CA par **segment RFM** (clients récents / fidèles / à risque) pour identifier les leviers de croissance.
   """)

   ###################################################

elif page == pages[1]:
   df = pd.read_csv('exploration.csv')
   df_rfm1 = pd.read_csv("df_rfm1.csv")
   df_rfm2 = pd.read_csv("df_rfm2.csv")
   pd.set_option('display.max_columns', None)
   df['Created_at'] = pd.to_datetime(df['Created_at'])
   df['Customer since'] = pd.to_datetime(df['Customer since']).dt.to_period('M')
   df_rfm = pd.read_csv("df_rfm.csv")
   
   st.markdown("<h2 style='font-weight:lighter; text-align: center; font-size: 60px;text-shadow: -1px -1px #000, 1px 1px #000, -3px 0 4px #000;'>Mise en oeuvre de la méthode RFM</h2>", unsafe_allow_html=True)
   st.markdown(" <br><br>", unsafe_allow_html=True)
   
   st.markdown("<h2 style='text-align: center; font-size:15'>Calcul des composantes RFM</h2>", unsafe_allow_html=True)
   st.markdown("<br>", unsafe_allow_html=True)
   
   col1, col2,col3 = st.columns([1,3,1])
   with col1:
      ""
   with col2:
      hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
      st.markdown(hide_table_row_index, unsafe_allow_html=True)
      st.table(df_rfm.head()) 

   with col3:
      ""
   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("<h2 style='text-align: center; font-size:15'>1ère approche de clustering</h2>", unsafe_allow_html=True)


   st.write("Le score RFM est calculé en fonction de la récence, de la fréquence et des classements de normalisation de la valeur monétaire. Sur la base de ce score, nous divisons nos clients. Ici, nous les notons sur une échelle de 5. La formule utilisée pour calculer le score rfm est : 0,15 X Score de récence + 0,28 X Score de fréquence + 0,57 X Score monétaire")
   st.markdown("<br>", unsafe_allow_html=True)
   hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
   st.markdown(hide_table_row_index, unsafe_allow_html=True)
    
   st.table(df_rfm1.head())
 
   df_analysis_rfm1 = df_rfm1.groupby('Customer_segment').agg({'Customer_segment':'count'})

   df_analysis_rfm1.rename({'Customer_segment':'Total_customer_id'}, axis=1, inplace=True)
   df_analysis_rfm1['count_share'] = ((df_analysis_rfm1['Total_customer_id'] / df_analysis_rfm1['Total_customer_id'].sum()) * 100).round(2)
   df_analysis_rfm1.sort_values(by='Total_customer_id', ascending=False)
   st.markdown(" <br>", unsafe_allow_html=True)
    
    
    
   fig, ax = plt.subplots(figsize=(16,6))
   labels = df_analysis_rfm1.index + df_analysis_rfm1['count_share'].apply(lambda x: ' ' + str(x) + ' %')
   fig, ax = plt.subplots(figsize=(16,6))
   squarify.plot(sizes=df_analysis_rfm1['count_share'], label=labels, alpha=.8, color=colors)
   ax.set_title('Répartition des différents clusters', fontsize=20, color='b')
   plt.axis('off');
   st.pyplot(fig)



   st.markdown(" <br><br>", unsafe_allow_html=True)
   st.markdown("<h2 style='text-align: center; font-size:15'>2ème approche de clustering</h2>", unsafe_allow_html=True)

   st.write("Dans cette approche nous appliquons une approche basée sur un système de points affectés à chaque client en fonction du quintile auquel il appartient pour chaque composante RFM")
    
   st.markdown(" <br>", unsafe_allow_html=True)
   st.markdown("<br>", unsafe_allow_html=True)
   hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
   st.markdown(hide_table_row_index, unsafe_allow_html=True)
   st.table(df_rfm2.head())
    
   st.markdown(" <br>", unsafe_allow_html=True)
   
   #Création de df_analysis
   df_analysis = df_rfm2.groupby('Label').agg({'Label':'count'})
   df_analysis.rename({'Label':'Total_customer_id'}, axis=1, inplace=True)
   df_analysis['count_share'] = ((df_analysis['Total_customer_id'] / df_analysis['Total_customer_id'].sum()) * 100).round(2)

   df_analysis.sort_values(by='Total_customer_id', ascending=False)
      
   labels = df_analysis.index + df_analysis['count_share'].apply(lambda x: ' ' + str(x) + ' %')

   fig, ax = plt.subplots(figsize=(16,6))
   squarify.plot(sizes=df_analysis['count_share'], label=labels, alpha=.8, color=colors)
   ax.set_title('Répartition des différents clusters', fontsize=20, color='b')
   plt.axis('off')
   st.pyplot(fig)


elif page == pages[2]:
   df = pd.read_csv('exploration.csv')
   df_rfm2 = pd.read_csv("df_rfm2.csv")
   pd.set_option('display.max_columns', None)
   df['Created_at'] = pd.to_datetime(df['Created_at'])
   df['Customer since'] = pd.to_datetime(df['Customer since']).dt.to_period('M')
   df2 = pd.read_csv('df2.csv',index_col='Customer_id')
   pd.set_option('display.max_columns', None)
   df2['Created_at'] = pd.to_datetime(df2['Created_at'])
   df2['Customer since'] = pd.to_datetime(df2['Customer since']).dt.to_period('M')
   st.markdown("<h2 style='font-weight:lighter; text-align: center; font-size: 60px;text-shadow: -1px -1px #000, 1px 1px #000, -3px 0 4px #000;'>Analyse des Clusters</h2>", unsafe_allow_html=True)
   st.markdown(" <br>", unsafe_allow_html=True)
   
   activation_function = st.selectbox("Choix du cluster", [" ","Top Customer", "Client dilemme","Client à potentiel élevé", "Client à surveiller","Client sans potentiel stratégique"])
   
    
# choix sans titre
   if activation_function == " ":
      st.markdown("<h2 style='text-align: center; font-size:15'>Distribution des clusters</h2>", unsafe_allow_html=True)
      st.markdown(" <br><br>", unsafe_allow_html=True)
      fig= plt.figure(figsize=(10,5))
      ax = fig.add_subplot()
        
      sns.countplot(df_rfm2["Label"], palette = colors)
      total = float(len(df_rfm2["Label"]))
      for p in ax.patches:
         height = p.get_height()
         ax.annotate( "{:.2f}%".format(100 * p.get_height()/total),(p.get_x() + p.get_width()/2, height+.05),
                             ha="center",va="bottom",fontsize=10)             
      plt.xticks(rotation = 45)
      plt.xlabel("")
      st.pyplot(fig)
    
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<h2 style='text-align: center; font-size:15'>Profils des clusters</h2>", unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      fig = sns.lmplot(x='Recency', y='Frequency', data=df_rfm2, hue='Label', col='Label')
      fig.set_titles("{col_name}",size = 20)
      fig.set_xlabels(size = 20)
      fig.set_ylabels(size = 20)
      st.pyplot(fig)
 
      fig = sns.lmplot(x='Recency', y='Monetary', data=df_rfm2, col='Label', hue='Label')
      fig.set_titles("{col_name}", size = 20)
      fig.set_xlabels(size = 20)
      fig.set_ylabels(size = 20)
      st.pyplot(fig)
        

      fig = sns.lmplot(x='Monetary', y='Frequency', data=df_rfm2, col='Label', hue='Label')
      fig.set_titles("{col_name}",size = 20)
      fig.set_xlabels(size = 20)
      fig.set_ylabels(size = 20)
      st.pyplot(fig);
       


# pour client dilemme
   st.markdown(" <br><br>", unsafe_allow_html=True)
   if activation_function == "Client dilemme":
      st.markdown("<h2 style='text-align: center;'>Analyse du comportement</h2>", unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
        
      col1, col2 = st.columns(2)
      fig = plt.figure(figsize=(15,10))
      with col1:
         fig = plt.figure(figsize=(15,10))

         df_dilemme = df2[df2["Label"]=="Client dilemme"]
         df_discount_dilemme_status = pd.crosstab(df_dilemme['Category'], df_dilemme['Regroupement_status'])
         df_discount_dilemme = pd.crosstab(df_dilemme['Category'], df_dilemme['Discount_amount_euros'] ==0, normalize=0).round(2)
         df_discount_dilemme.columns = ['Avec_remise', 'Sans_remise']
         df_discount_dilemme['nb_commande'] = df_dilemme['Category'].value_counts()
         df_discount_dilemme = df_discount_dilemme.merge(df_discount_dilemme_status, left_index=True, right_index=True)
            
         plt.plot(df_discount_dilemme.index, df_discount_dilemme['Avec_remise'])
         plt.xticks(rotation=45, horizontalalignment='right', fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylim(0,1)
         plt.ylabel("Taux d'achats remisés", fontsize = 30, color="b")
         plt.title("Impact des remises sur les achats", fontsize = 40, color="b")
         st.pyplot(fig)
      with col2 :
         fig = plt.figure(figsize=(15,10))


         plt.bar(df_discount_dilemme.index, df_discount_dilemme['annulé'], label='annulé', color="#e31a1c")
         plt.bar(df_discount_dilemme.index, df_discount_dilemme['finalisé'], bottom=df_discount_dilemme['annulé'],
                                                label='finalisé', color="#33a02c")
         plt.xticks(rotation=45, horizontalalignment='right',fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylabel('Volumes de commandes', color='b', fontsize=30)
         plt.title("Volume de commandes", fontsize = 40, color ="b")
         plt.legend(fontsize=20)
         st.pyplot(fig)
            
            
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Observations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Leur volume d'achat est déjà important. Exception faite des mobiles et tablettes, ils sont peu sensibles aux promotions. Cependant on constate que leurs achats sont axés sur les articles de mode, de beauté, ainsi que des mobiles et tablettes.</p>",unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Recommandations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Notre but n’est pas de les fidéliser ni de changer leurs habitudes de consommation, mais d’augmenter leur nombre, ce qui permettra de générer un chiffre d’affaires plus important. Pour ce faire nous proposons de communiquer sur les articles à succès (articles de modes, beauté, mobiles et tablettes).</p>",unsafe_allow_html=True)

 
        
# pour Top Customer
   st.markdown(" <br>", unsafe_allow_html=True)
   if activation_function == "Top Customer":
      st.markdown("<h2 style='text-align: center;'>Analyse du comportement</h2>", unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      df_top = df2[df2["Label"]=="Top Customer"]       
      df_discount_top_status = pd.crosstab(df_top['Category'], df_top['Regroupement_status'])

      df_discount_top = pd.crosstab(df_top['Category'], df_top['Discount_amount_euros'] ==0, normalize=0).round(2)
      df_discount_top.columns = ['Avec_remise', 'Sans_remise']
      df_discount_top['nb_commande'] = df_top['Category'].value_counts()
      df_discount_top = df_discount_top.merge(df_discount_top_status, left_index=True, right_index=True)
        
      col1, col2 = st.columns(2)
      fig = plt.figure(figsize=(15,10))
      with col1:
         fig = plt.figure(figsize=(15,10))
         plt.plot(df_discount_top.index, df_discount_top['Avec_remise'])
         plt.xticks(rotation=45, horizontalalignment='right', fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylim(0,1)
         plt.ylabel("Taux d'achats remisés", fontsize = 30, color="b")
         plt.title("Impact des remises sur les achats", fontsize = 40, color="b")
         st.pyplot(fig)
      with col2 :
         fig = plt.figure(figsize=(15,10))
         #st.markdown("Volume de commandes")

         plt.bar(df_discount_top.index, df_discount_top['annulé'], label='annulé', color="#e31a1c")
         plt.bar(df_discount_top.index, df_discount_top['finalisé'], bottom=df_discount_top['annulé'],
                                 label='finalisé', color="#33a02c")
         plt.xticks(rotation=45, horizontalalignment='right',fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylabel('Volumes de commandes', color='b', fontsize=30)
         plt.title("Volume de commandes", fontsize = 40, color ="b")
         plt.legend(fontsize=20)
         st.pyplot(fig)    
         st.markdown(" <br><br>", unsafe_allow_html=True)
    #Volume en net income
      top1= df_top.groupby(df_top['Category']).agg({"Net_income_euros" : "sum"})
      fig = plt.figure(figsize=(15,10))
      plt.bar(top1.index, top1["Net_income_euros"])
      plt.xticks(rotation=45, horizontalalignment='right', fontsize =15)
      plt.yticks(fontsize =15)
      plt.ylabel("Chiffre d'affaires en K€")
      plt.title("Chiffre d'affaires par Catégorie", fontsize = 20, color="b")
      st.pyplot(fig)
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Observations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Ce sont des clients qui présentent un profil de consommation homogéne sur la fréquence d'achat, la récence des visites et le montant des dépenses.</p>",unsafe_allow_html=True)
      
      st.markdown("<br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px;font-weight: bold'>Recommandations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Nous ne souhaitons pas de transformation de ces clients fidèles, réguliers et bons consommateurs.</p>",unsafe_allow_html=True)   
        
        
# pour clientà surveiller
   if activation_function == "Client à surveiller":
      st.markdown("<h2 style='text-align: center;'>Analyse du comportement</h2>", unsafe_allow_html=True)
      df_a_surveiller = df2[df2["Label"]=="Client à surveiller"]       
      df_discount_a_surveiller_status = pd.crosstab(df_a_surveiller['Category'], df_a_surveiller['Regroupement_status'])

      df_discount_a_surveiller = pd.crosstab(df_a_surveiller['Category'], df_a_surveiller['Discount_amount_euros'] ==0, normalize=0).round(2)
      df_discount_a_surveiller.columns = ['Avec_remise', 'Sans_remise']
      df_discount_a_surveiller['nb_commande'] = df_a_surveiller['Category'].value_counts()
      df_discount_a_surveiller = df_discount_a_surveiller.merge(df_discount_a_surveiller_status, left_index=True, right_index=True)
      st.markdown("<br>", unsafe_allow_html=True)
        
      col1, col2 = st.columns(2)
      fig = plt.figure(figsize=(15,10))
      with col1:
         fig = plt.figure(figsize=(15,10))
         plt.plot(df_discount_a_surveiller.index, df_discount_a_surveiller['Avec_remise'])
         plt.xticks(rotation=45, horizontalalignment='right', fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylim(0,1)
         plt.ylabel("Taux d'achats remisés", fontsize = 30, color="b")
         plt.title("Impact des remises sur les achats", fontsize = 40, color="b")
         st.pyplot(fig)
      with col2:
         fig = plt.figure(figsize=(15,10))
         #st.markdown("Volume de commandes")

         plt.bar(df_discount_a_surveiller.index, df_discount_a_surveiller['annulé'], label='annulé', color="#e31a1c")
         plt.bar(df_discount_a_surveiller.index, df_discount_a_surveiller['finalisé'], bottom=df_discount_a_surveiller['annulé'],
                                 label='finalisé', color="#33a02c")
         plt.xticks(rotation=45, horizontalalignment='right',fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylabel('Volumes de commandes', color='b', fontsize=30)
         plt.title("Volume de commandes", fontsize = 40, color ="b")
         plt.legend(fontsize=20)
         st.pyplot(fig)       
            
            
      df_comparaison = df2.loc[(df2['Label']=='Client à surveiller') | (df2['Label']=='Top Customer')]
      df_comparaison2 = pd.crosstab(df_comparaison['Category'], df_comparaison['Label'])
      df_comparaison2 = df_comparaison2.reindex(df_comparaison['Category'].unique())
        
        
      st.markdown("<br>", unsafe_allow_html=True)
      fig=plt.figure(figsize=(10,7))
      sns.countplot(df_comparaison["Category"], palette = "Paired", hue = df_comparaison["Label"])
      plt.plot(df_comparaison['Category'].unique(), df_comparaison2['Client à surveiller'], c='#1f78b4')
      plt.plot(df_comparaison['Category'].unique(), df_comparaison2['Top Customer'], c='#a6cee3')
      plt.xticks(rotation=45, horizontalalignment="right")
      plt.title("Comparaison entre les achats des clients à surveiller et des top customers", fontsize=20, color="b")
      st.pyplot(fig)
        
        
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Observations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>La comparaison avec les comportements d'achat des top customers nous amène à penser qu'ils ont les mêmes profils de consommation. Exception faite des mobiles et tablettes qui présentent des volumes de ventes et un taux d’annulation particulièrement élevés, les achats s’orientent vers d’autres catégories peu sujettes à promotions (mens’ fashion et Soghaat).</p>",unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px;font-weight: bold'>Recommandations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Nous proposons ainsi de communiquer sur des produits d’appels, et des nouveautés sur ces catégories afin de conquérir ces clients.</p>",unsafe_allow_html=True)
    
        

# pour client à potentiel élevé
   if activation_function == "Client à potentiel élevé":
      st.markdown("<h2 style='text-align: center;'>Analyse du comportement</h2>", unsafe_allow_html=True)
      st.markdown(" <br><br>", unsafe_allow_html=True)
      df_potentiel_eleve = df2[df2["Label"]=="Client à potentiel élevé"]
      df_discount_potentiel_status = pd.crosstab(df_potentiel_eleve['Category'], df_potentiel_eleve['Regroupement_status'])

      df_discount_potentiel = pd.crosstab(df_potentiel_eleve['Category'], df_potentiel_eleve['Discount_amount'] ==0, normalize=0).round(2)
      df_discount_potentiel.columns = ['Avec_remise', 'Sans_remise']
      df_discount_potentiel['nb_commande'] = df_potentiel_eleve['Category'].value_counts()
      df_discount_potentiel = df_discount_potentiel.merge(df_discount_potentiel_status, left_index=True, right_index=True)

      col1, col2 = st.columns(2)
      fig = plt.figure(figsize=(15,10))
      with col1:
         fig = plt.figure(figsize=(15,10))
         plt.plot(df_discount_potentiel.index, df_discount_potentiel['Avec_remise'])
         plt.xticks(rotation=45, horizontalalignment='right', fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylim(0,1)
         plt.ylabel("Taux d'achats remisés", fontsize = 30, color="b")
         plt.title("Impact des remises sur les achats", fontsize = 40, color="b")
         st.pyplot(fig)
      with col2 :
         fig = plt.figure(figsize=(15,10))
         plt.bar(df_discount_potentiel.index, df_discount_potentiel['annulé'], label='annulé', color="#e31a1c")
         plt.bar(df_discount_potentiel.index, df_discount_potentiel['finalisé'], bottom=df_discount_potentiel['annulé'],
                                        label='finalisé', color="#33a02c")
         plt.xticks(rotation=45, horizontalalignment='right',fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylabel('Volumes de commandes', color='b', fontsize=30)
         plt.title("Volume de commandes", fontsize = 40, color ="b")
         plt.legend(fontsize=20)
         st.pyplot(fig)  
            
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Observations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>On constate que le volume des ventes des clients à potentiel élevés est moins important que celui des clients dilemmes.On remarque aussi qu'ils sont sensibles aux promotions.</p>",unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px;font-weight: bold'>Recommandations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Nous souhaitons augmenter leur consommation afin qu’ils puissent devenir des Top Customer. Compte tenu de leur sensibilité aux promotions, une piste serait de leur proposer des opérations promotionnelles exclusives et ciblées afin de stimuler leurs achats.</p>",unsafe_allow_html=True)
       
# pour client Sans potentiel Stratégique
   if activation_function == "Client sans potentiel stratégique":
      st.markdown("<h2 style='text-align: center;'>Analyse du comportement</h2>", unsafe_allow_html=True) 
      st.markdown("<br>", unsafe_allow_html=True)  
            
      df_sans_potentiel = df2[df2["Label"]=="Client sans potentiel stratégique"]
      df_discount_sans_potentiel_status = pd.crosstab(df_sans_potentiel['Category'], df_sans_potentiel['Regroupement_status'])
      df_discount_sans_potentiel = pd.crosstab(df_sans_potentiel['Category'],df_sans_potentiel['Discount_amount'] ==0, normalize=0).round(2)
      df_discount_sans_potentiel.columns = ['Avec_remise', 'Sans_remise']
      df_discount_sans_potentiel['nb_commande'] = df_sans_potentiel['Category'].value_counts()
      df_discount_sans_potentiel = df_discount_sans_potentiel.merge(df_discount_sans_potentiel_status, left_index=True, right_index=True)

      col1, col2 = st.columns(2)
      fig = plt.figure(figsize=(15,10))
      with col1:
         fig = plt.figure(figsize=(15,10))
         plt.plot(df_discount_sans_potentiel.index, df_discount_sans_potentiel['Avec_remise'])
         plt.xticks(rotation=45, horizontalalignment='right', fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylim(0,1)
         plt.ylabel("Taux d'achats remisés", fontsize = 30, color="b")
         plt.title("Impact des remises sur les achats", fontsize = 40, color="b")
         st.pyplot(fig)
      with col2:
         fig = plt.figure(figsize=(15,10))

         plt.bar(df_discount_sans_potentiel.index, df_discount_sans_potentiel['annulé'], label='annulé', color="#e31a1c")
         plt.bar(df_discount_sans_potentiel.index, df_discount_sans_potentiel['finalisé'], bottom=df_discount_sans_potentiel['annulé'],
                                        label='finalisé', color="#33a02c")
         plt.xticks(rotation=45, horizontalalignment='right',fontsize =30)
         plt.yticks(fontsize =30)
         plt.ylabel('Volumes de commandes', color='b', fontsize=30)
         plt.title("Volume de commandes", fontsize = 40, color ="b")
         plt.legend(fontsize=20)
         st.pyplot(fig)        
      st.markdown(" <br><br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px; font-weight: bold'>Observations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Client qui n'est pas venu récemment, n'est pas régulier, donc n'a aucun intérêt stratégique, peu importe le montant de ses achats.</p>",unsafe_allow_html=True)
      st.markdown("<br>", unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 22px;font-weight: bold'>Recommandations :</p>",unsafe_allow_html=True)
      st.markdown("<p style = 'font-size : 17px;text-align: justify'>Il est complexe d'établir des préconnisations pour ce cluster sur lequel nous ne disposons pas encore d'assez de données au niveau de la récence.</p>",unsafe_allow_html=True)
else:
   st.markdown("<h2 style='font-weight:lighter; text-align: center; font-size: 60px;text-shadow: -1px -1px #000, 1px 1px #000, -3px 0 4px #000;'>Conclusion</h2>", unsafe_allow_html=True)
   st.markdown("<p style = 'font-size : 17px;text-align: justify'><br><br>Notre modèle nous apparait comme concret, flexible et personnalisable à volonté. Par ailleurs il reste relativement simple à appliquer et mettre en œuvre au sein d’entreprises de divers secteurs.<br><br>La démarche appliquée et le modèle qui en résulte ne se limitent pas à la seule application qui en est faite ici. Il est tout à fait possible de l’adapter à de nombreux autres sujets (classification en trois composantes différentes de celles de la RFM).<br><br></p>",unsafe_allow_html=True)
   st.markdown("<p style = 'font-size : 17px;text-align: justify;font-weight: bold'>Il serait possible d’améliorer la méthode d’analyse proposée en comparant :<br></p>",unsafe_allow_html=True)


   #st.write("The following list won’t indent no matter what I try:")
   st.markdown("- Évolution chronologique des clusters")
   st.markdown("- Exploitation d'autres composantes (non exploitées à date)")
   st.markdown("- Perfectionnement des data visualisations")
   st.markdown(''' <style> [data-testid="stMarkdownContainer"] ul{padding-left:40px;} </style> ''', unsafe_allow_html=True)
    
                   




































# Display settings for the stock market simulation
DISPLAY_SETTINGS = {
    "figsize": (12, 8),
    "title": "Cours des Bières",
    "title_fontsize": 16,
    "title_fontweight": 'bold',
    "xlabel": "Temps",
    "xlabel_fontsize": 12,
    "ylabel": "Prix (€)",
    "ylabel_fontsize": 12,
    "legend_loc": 'upper left',
    "legend_fontsize": 10,
    "grid_linestyle": '--',
    "grid_linewidth": 0.5,
    "marker": '.',
    "linestyle": '-',
    "markersize": 4,
    "text_fontsize": 9,
    "logo_path": "logo_comif.png",
    "logo_zoom": 0.2,
    "logo_position": (0.5, 0.5),
    "left_margin": 0.17,
    "right_margin": 0.9,
    "top_margin": 0.9,
    "bottom_margin": 0.13,
}

from bourse import Market, Stock, Agent

TIME_INTERVAL = 5  # intervalle de temps
PRICE_HISTORY_LENGTH = 5000  # longueur de l'historique
DISPLAY_WINDOW_LENGTH = 75  # Longueur de la fenêtre d'affichage


# prix initiaux bieres
stocks = [
    Stock("Piraat ", 2.9, 2.0, color='red'),
    Stock("Double rousse", 2.7, 2, color='blue'),
    Stock("Petite aixoise", 2.1, 1.4, color='green'),
    Stock("None",0, 0, color='purple'),
]

market = Market(stocks)
agent = Agent("Martin", market)


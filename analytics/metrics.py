
# Function to calculate the average points a defense allows to a certain position
def get_points_allowed_by_position(stats_df, team_abbr, position):
    filtered = stats_df.filter((stats_df["opponent_team"] == team_abbr) & (stats_df["position"] == position))
    return filtered["fantasy_points_ppr"].mean() # FIX LATER (SHOULDN'T JUST BE PPR)
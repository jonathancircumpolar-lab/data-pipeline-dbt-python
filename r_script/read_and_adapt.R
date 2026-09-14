library(readr)
library(dplyr)

data <- read_csv("exports/mart_missions_by_site.csv")

summary_by_status <- data %>%
  group_by(site_id) %>%
  summarise(total = sum(parcel_count))

print(summary_by_status)

write_csv(summary_by_status, "r_script/summary_by_site.csv")
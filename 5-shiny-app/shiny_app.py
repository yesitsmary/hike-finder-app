from shiny import App, ui, render
import requests

# Dropdown choices
energy_levels = ["Relaxed", "Chill", "Adventurous", "Challenging"]
parks = [
    "Acadia", "Arches", "Badlands", "Big Bend", "Bryce Canyon", "Canyonlands",
    "Carlsbad Caverns", "Cuyahoga Valley", "Death Valley", "Glacier Bay",
    "Grand Teton", "Great Basin", "Great Smoky Mountains", "Guadalupe Mountains",
    "Haleakalā", "Hawaiʻi Volcanoes", "Hot Springs", "Indiana Dunes", "Joshua Tree",
    "Katmai", "Lassen Volcanic", "Mount Rainier", "New River Gorge", "North Cascades",
    "Pinnacles", "Redwood", "Rocky Mountain", "Sequoia & Kings Canyon", "Shenandoah",
    "Theodore Roosevelt", "Virgin Islands", "Voyageurs", "Wind Cave", "Yellowstone",
    "Yosemite", "Zion"
]

app_ui = ui.page_fluid(
    ui.h2("🏞️ Find a Hiking Trail"),
    ui.input_select("energy", "Select your energy level:", choices=energy_levels),
    ui.input_select("park", "Select National Park:", choices=parks),
    ui.output_ui("trail_output")
)

def server(input, output, session):
    @output
    @render.ui
    def trail_output():
        description = f"Looking for a {input.energy().lower()} hike in {input.park()}"
        url = "https://hike-finder-api-306102299544.us-central1.run.app/predict"

        try:
            response = requests.post(url, json={
                "longDescription": description,
                "parkName": f"{input.park()} National Park"
            })
            response.raise_for_status()
            data = response.json()

            title = data.get("title", "Sorry!")
            short_desc = data.get("shortDescription", "It looks the NPS does not have trails for these categories.")
            duration = data.get("duration", "")
            url = data.get("url", "")

            return ui.div(
                ui.h4(title),
                ui.p(short_desc),
                ui.p(f"Duration: {duration}"),
                ui.a("More details", href=url, target="_blank") if url else ui.span()  # safe fallback
            )

        except requests.exceptions.RequestException as e:
            return ui.div(ui.p(f"Error: {str(e)}"))

app = App(app_ui, server)
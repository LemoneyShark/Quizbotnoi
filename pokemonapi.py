from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

# สร้างโมเดลเพื่อรับค่าจากการ request
class PokemonRequest(BaseModel):
    id: int

# ฟังก์ชันเพื่อดึงข้อมูลจาก PokeAPI
def get_pokemon_data(id: int):
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{id}/"
    pokemon_form_url = f"https://pokeapi.co/api/v2/pokemon-form/{id}/"

    # เรียกข้อมูลจาก API
    pokemon_response = requests.get(pokemon_url)
    pokemon_form_response = requests.get(pokemon_form_url)

    # ตรวจสอบว่า API ส่งข้อมูลสำเร็จหรือไม่
    if pokemon_response.status_code == 200 and pokemon_form_response.status_code == 200:
        pokemon_data = pokemon_response.json()
        pokemon_form_data = pokemon_form_response.json()

        # รวมข้อมูลทั้งสองส่วนใน dictionary เดียว
        combined_data = {
            "pokemon": pokemon_data,
            "pokemon_form": pokemon_form_data
        }

        return combined_data
    else:
        raise HTTPException(status_code=404, detail="Data not found from PokeAPI")

# สร้าง route สำหรับรับ POST method
@app.post("/get_pokemon")
async def get_pokemon(request: PokemonRequest):
    id = request.id

    # เรียกฟังก์ชันดึงข้อมูลจาก PokeAPI
    pokemon_data = get_pokemon_data(id)

    # ส่งข้อมูลกลับในรูปแบบ JSON
    return pokemon_data


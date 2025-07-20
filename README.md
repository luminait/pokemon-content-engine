# pokemon-content-engine

[![AI-Powered](https://img.shields.io/badge/AI-RAG-blue)](https://openai.com/)
[![n8n](https://img.shields.io/badge/Workflow-n8n-orange)](https://n8n.io/)
[![Shotstack](https://img.shields.io/badge/Video-Generation-yellow)](https://shotstack.io/)

---

## Overview

**pokemon-content-engine** is an AI-RAG-powered content creation engine for Deez Collectibles. It generates targeted social media campaign blueprints and unique posts by leveraging customer personas, campaign templates, and advanced AI agents. The system enables precise campaign targeting, dynamic character and scene selection, and automated post generation, ensuring each campaign maintains a consistent message and creative flair. Integration with Shotstack and OpenAI enables seamless video and image content creation.

---

## Table of Contents

- [Features](#features)
- [Engine Resources](#engine-resources)
- [Workflow](#workflow)
  - [Campaign Generation](#campaign-generation)
  - [Post Generation](#post-generation)
  - [Shotstack Integration (Stub)](#shotstack-integration-stub)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- AI-driven campaign blueprint generation tailored to specific customer personas
- Dynamic character, scene, and asset selection
- Automated post creation with unique dialogue and character variations
- Resource-driven RAG knowledge base (personas, templates, prompts)
- Modular workflow for campaign and post generation
- Planned integration with Shotstack for video rendering

---

## Engine Resources

- **Customer Personas** (`content-engine/resources/customer_personas/`)
  - `customer_persona_Hardcore_Collector.md`
  - `customer_persona_Nostalgic_Collector.md`
  - `customer_persona_Status_Seeker.md`
- **Templates** (`content-engine/resources/templates/`)
  - `campaign_blueprint_template.md`
  - `post_template.md`
- **Prompts** (`content-engine/resources/prompts/`)
  - `campaign_generator.md`
  - `post_generator.md`

---

## Workflow

### Campaign Generation

1. **Persona Selection:** Choose one or more customer personas.
2. **Character Assets:** Select character asset IDs (from `character_assets_database.csv`).
3. **Character Merge-Fields:** Define merge fields and set `max_characters_per_post`.
4. **Character Pool Creation:** Assign roles and scene hints to selected characters.
5. **Environment Assets:** Select scene/environment asset IDs.
6. **Target Length:** Specify desired post length (seconds).
7. **Campaign Name:** Provide or auto-generate a unique campaign name.
8. **Call-to-Action:** Define the campaign's primary call-to-action.
9. **Tagline:** Specify any required tagline or message.
10. **Content Type:** Indicate dialog source (characters or narrator).
11. **Campaign Description:** Provide narrative context.
12. **Cadence:** Set campaign days (e.g., monday, wednesday).

Campaign generator outputs a campaign blueprint using `campaign_blueprint_template.md`.

---

### Post Generation

1. **Campaign Selection:** Choose a campaign from `campaign_ids.csv`.
2. **Character Assets:** Select characters from the campaign’s pool (max: `max_characters_per_post`).
   - **Narrative Intent:** Assign a narrative purpose for each character.
3. **Environment Assets:** Select relevant scene/environment assets.
4. **Confirm Character Assets:** Optionally omit characters for this post.
5. **Target Length:** Confirm or adjust the post’s target length.
6. **Featured Cards:** Specify featured cards or opt for narrative-only content.
7. **Special Instructions:** Add any specific instructions for the post.

Post generator produces a post using `post_template.md`.

---

### Shotstack Integration (Stub)

> **Planned:**  
> After post creation, the system will generate Shotstack JSON and call the Shotstack API to render video content. Users will be prompted to approve or regenerate the video before submission to social media.

---

## Installation

> **Note:**  
> Installation and setup instructions will be provided upon finalization of the implementation approach.

---

## Contributing

This project is developed and maintained solely by the author for a specific client. Pull requests and external contributions are not accepted.

---

## License

This repository and its contents are proprietary and confidential.  
All rights reserved. Unauthorized use, distribution, or modification is strictly prohibited.

---

**Contact:**  
For inquiries, please contact the repository owner directly.

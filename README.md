# WixossImportTool

This repository contains a collection of scripts to import and export Wixoss cards from different contexts. This includes: from the official database to a `.csv` or `.tsv` file, from a  `.tsv`
into tabletop simulator, from different deckbuilding sites to a JSON string and from a JSON string into Tabletop Simulator. Cards included are only the ones released in english.

## How to import decks into Tabletop Simulator

This section will explain how to import your Wixoss decks from deckbuilding sites such as [DeXoss](https://dexoss.app/home) or [wixosstcg.eu](https://www.wixosstcg.eu) into the Tabletop Simulator mod.

### Step 1: Install a user script manager browser extension.

In order to make the user experience friendly, I developed a user script that makes an export button appear on deckbuilding sites. To install it, you first need to install a user script manager.
In the table below you can find the most popular script managers for the most popular browsers. The script has only been tested with ViolentMonkey.

|               | Chrome                                                                                                  | Firefox                                                               | Safari                                                | Edge                                                                                                           | Opera                                                                        |
|---------------|---------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| ViolentMonkey | [click here](https://chrome.google.com/webstore/detail/violent-monkey/jinjaccalgkegednnccohejagnlnfdag) | [click here](https://addons.mozilla.org/firefox/addon/violentmonkey/) |                                                       | [click here](https://microsoftedge.microsoft.com/addons/detail/violentmonkey/eeagobfjdenkkddmbclomhiblgggliao) | [click here](https://violentmonkey.github.io/get-it/)                        |
| TamperMonkey  | [click here](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)   | [click here](https://addons.mozilla.org/firefox/addon/tampermonkey/)  | [click here](http://tampermonkey.net/?browser=safari) | [click here](https://microsoftedge.microsoft.com/addons/detail/tampermonkey/iikmkjmpaadaobahmlepeloendndfphd)  | [click here](https://addons.opera.com/extensions/details/tampermonkey-beta/) |
| GreaseMonkey  |                                                                                                         | [click here](https://addons.mozilla.org/firefox/addon/greasemonkey/)  |                                                       |                                                                                                                |                                                                              |

### Step 2: Install the Wixoss Exporter user script

Once you have a script manager installed. You can install the Wixoss Deck Exporter from [GreasyFork](https://greasyfork.org/en/scripts/474626-wixoss-tabletop-simulator-exporter).
You can see the source code [here](https://github.com/ShonTitor/WixossImportTool/blob/main/browser_exporter.js).
The user script only has permission to act on [DeXoss](https://dexoss.app/home) and [wixosstcg.eu](https://www.wixosstcg.eu) and only in the individual deck pages.

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/c043744b-3f3f-4b17-8481-e00a1f525cbf)

### Step 3: Export your deck to JSON

Once the user script is installed, go to your preferred deckbuilding site (either [DeXoss](https://dexoss.app/home) or [wixosstcg.eu](https://www.wixosstcg.eu))
and open the deck you want to export. If the script is working correctly, you'll see a "Export to TTS button".

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/4a4d9bde-f1b5-409e-81ee-67656d996782)

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/e7dd277c-bdd8-4e51-889a-cc5506290374)

If you click on this button, a modal will be displayed containing your deck in JSON format. Copy this code for later use.

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/e35455e8-b86b-4e7f-8ef6-fd6b3fbbfe0c)

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/aa981795-153f-4035-8b13-8b67b61c30a3)

### Step 4: Paste the code on Tabletop Simulator

Click on the notebook icon in Tabletop Simulator and paste the code you copied in the "myDeck" notebook (replace the previous contents).
Don't change the name of the notebook to ensure the correct functioning of the deck importer.

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/51ed2959-3deb-4ce3-8a95-c1a80f983f37)

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/25675dbd-1890-409b-8bf9-96a1db4f52aa)

### Step 5: Import the deck

Go to the wixoss deck importer (the black hole in the corner) and click the button in the middle.
The game may slow down a little, this is normal. Do not move the cards until the deck is done importing.
You deck will spawn on the table next to the importer. Cards in the deck can be searched by name, card number and type.

![image](https://github.com/ShonTitor/WixossImportTool/assets/39103403/83bcb326-cc96-479a-acfe-40ce1c5ef391)

### Step 6: Have Fun

Thank you so much for you interest on this alternative to play Wixoss online.
If you wish to support me you can do so on my [ko-fi](https://ko-fi.com/riokaru).

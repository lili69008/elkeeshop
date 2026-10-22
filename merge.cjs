const fs = require('fs');

// Chemins des fichiers sources
const htmlPath = 'C:\\\\Users\\\\lyies\\\\Desktop\\\\shopages\\\\preview.html';
const cssPath = 'C:\\\\Users\\\\lyies\\\\Desktop\\\\shopages\\\\theme\\\\assets\\\\phoenix.css';
const jsPath = 'C:\\\\Users\\\\lyies\\\\Desktop\\\\shopages\\\\theme\\\\assets\\\\phoenix.js';

const html = fs.readFileSync(htmlPath, 'utf8');
const css = fs.readFileSync(cssPath, 'utf8');
const js = fs.readFileSync(jsPath, 'utf8');

// Extraction du contenu DOM
const domStart = html.indexOf('<div class="phx" id="phx-root"');
const domEnd = html.indexOf('<!-- ====', domStart);
const domContent = html.substring(domStart, domEnd);

// Extraction des données de configuration
const dataStart = html.indexOf('<script>');
const dataEnd = html.indexOf('</script>', dataStart) + 9;
const dataContent = html.substring(dataStart, dataEnd);

// Séparation de la balise ouvrante de la div racine pour injecter les styles à l'intérieur
const firstCloseBracket = domContent.indexOf('>');
const rootTag = domContent.substring(0, firstCloseBracket + 1);
const innerDomContent = domContent.substring(firstCloseBracket + 1);

// Nettoyage des commentaires pour éviter les bugs de parseur GemPages
const cleanCss = css.replace(/\/\*[\s\S]*?\*\//g, '').trim();
const cleanJs = js.replace(/\/\*[\s\S]*?\*\//g, '').trim();

// Compilation avec injection interne ultra-sécurisée pour GemPages
const finalCode = `<!-- DEBUT DU CODE CUSTOM GEMPAGES PHOENIX -->
${rootTag}
  <!-- Liens polices et styles injectés en interne pour contourner le nettoyage de GemPages -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Allura&family=Karla:ital,wght@0,400;0,700;1,400&family=Poppins:wght@300;400;500;600&family=Roboto:wght@400;700&display=swap">
  <style>
    ${cleanCss}
  </style>

  ${innerDomContent}

  ${dataContent}

  <script>
    ${cleanJs}
  </script>
<!-- FIN DU CODE CUSTOM GEMPAGES PHOENIX -->`;

fs.writeFileSync('C:\\\\Users\\\\lyies\\\\Desktop\\\\shopages\\\\CODE_FINAL_GEMPAGES.html', finalCode.trim());
console.log("Fichier CODE_FINAL_GEMPAGES.html cree et securise pour GemPages !");

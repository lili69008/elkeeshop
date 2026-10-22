from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
import os

def create_master_pdf():
    output_path = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/Elke_Berr_Validation_MASTER_Real_V2.pdf"
    capture_dir = "c:/Users/lyies/Desktop/siteelk/wireframes_pack/localhost_captures"
    
    # Sort files to ensure 01, 02, 03... order
    files = sorted([f for f in os.listdir(capture_dir) if f.endswith(".png")])
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    for i, filename in enumerate(files):
        img_path = os.path.join(capture_dir, filename)
        
        # Header Page
        c.setFont("Helvetica-Bold", 18)
        c.drawString(2*cm, height - 3*cm, f"PAGE {i+1} : {filename.replace('_V2.png', '').replace('_', ' ')}")
        
        c.setFont("Helvetica", 10)
        c.drawString(2*cm, height - 4*cm, "Identité Visuelle V2 — Prototype Haute Résolution")
        
        # Main Image (scaled to fit)
        # We use a large area to show the full page
        img_w = 16*cm
        img_h = 20*cm # Max height for preview
        c.drawImage(img_path, 2*cm, height - 25*cm, width=img_w, height=img_h, preserveAspectRatio=True)
        
        # Feedback Form Section
        c.rect(2*cm, 2*cm, 17*cm, 3*cm, fill=0)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(2.5*cm, 4.5*cm, "RETOURS ET CORRECTIONS CLIENT :")
        
        # Create a text field for interactive feedback
        form = c.acroForm
        field_name = f"feedback_{i+1}"
        form.textfield(name=field_name, tooltip=f"Saisissez vos retours pour {filename}",
                        x=2.5*cm, y=2.2*cm, width=16*cm, height=2.2*cm,
                        fontSize=10, borderStyle='inset', borderColor=None, fillColor=None)

        c.showPage()
    
    c.save()
    print(f"PDF Master Site Complet ({len(files)} pages) généré : {output_path}")

if __name__ == "__main__":
    create_master_pdf()

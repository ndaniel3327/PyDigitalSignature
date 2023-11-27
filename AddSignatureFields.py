from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers


signer = signers.SimpleSigner.load_pkcs12(
    'newpfxcertificate.pfx', passphrase=bytes('tenerife123', 'utf-8'))
with open('3signatureFields.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    #fields.append_signature_field(
    #    w, sig_field_spec=fields.SigFieldSpec(
    #        'Signature1'
    #    )
    #)
    #fields.append_signature_field(w,sig_field_spec=fields.SigFieldSpec('Signature2'))

    meta = signers.PdfSignatureMetadata(field_name='Sig1')
    pdf_signer = signers.PdfSigner(
        meta, signer=signer
        )
   
    with open('31signed.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)
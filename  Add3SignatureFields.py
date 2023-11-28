from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers

with open('31signed.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    fields.append_signature_field(w,sig_field_spec=fields.SigFieldSpec('Signature1'))
    fields.append_signature_field(w,sig_field_spec=fields.SigFieldSpec('Signature2'))
    fields.append_signature_field(w,sig_field_spec=fields.SigFieldSpec('Signature3'))

with open('32signed.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)
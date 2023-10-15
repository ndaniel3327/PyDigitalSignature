from pyhanko import stamp
from pyhanko.pdf_utils import text, images
from pyhanko.pdf_utils.font import opentype
from pyhanko.pdf_utils.incremental_writer import IncrementalPdfFileWriter
from pyhanko.sign import fields, signers


signer = signers.SimpleSigner.load_pkcs12(
    'newpfxcertificate.pfx', passphrase=bytes('tenerife123', 'utf-8'))
with open('output.pdf', 'rb') as inf:
    w = IncrementalPdfFileWriter(inf)
    fields.append_signature_field(
        w, sig_field_spec=fields.SigFieldSpec(
            'Signature', box=(100, 600, 300, 660)
        )
    )

    meta = signers.PdfSignatureMetadata(field_name='Signature')
    pdf_signer = signers.PdfSigner(
        meta, signer=signer, stamp_style=stamp.TextStampStyle(
            # the 'signer' and 'ts' parameters will be interpolated by pyHanko, if present
            stamp_text='Approved by the Führer. \nSigned by: %(signer)s\nTime: %(ts)s',
            text_box_style=text.TextBoxStyle(
                font=opentype.GlyphAccumulatorFactory(
                    'NotoSansRegular.ttf')
            ),
            background=images.PdfImage('mysignature.png')
        ),
    )
    with open('document-signed4.pdf', 'wb') as outf:
        pdf_signer.sign_pdf(w, output=outf)

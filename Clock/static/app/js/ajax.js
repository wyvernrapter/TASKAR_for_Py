function get_time() {
            // Ajax�ʐM����
            $.ajax({
                // ���N�G�X�g���M��URL�̐ݒ�
                url: '{% url "record_app:i_ajax" %}',�@�@# �����ŁAi_ajaxView���Ăяo���Ă���B
                // �񓯊��ʐM�t���O�itrue�͔񓯊��j
                async: true,
                // Ajax�ʐM�������Ƀ��X�|���X�f�[�^�󂯎��&�������s
                success: function(data) {�@�@�@�@�@�@�@�@
                    document.getElementById("datetime_auto").innerHTML = data;
                }
            });
        }
        // 1�b���ƂɎ��s����
        $(document).ready(function() {
            setInterval(get_time, 1000);
        });
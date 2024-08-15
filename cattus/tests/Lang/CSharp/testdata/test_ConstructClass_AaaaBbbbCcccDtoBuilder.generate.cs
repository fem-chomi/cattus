namespace AaaaBbbbCccc {

    public class AaaaBbbbCcccDtoBuilder {

        private sbyte eeeeFfffGggg;

        private short iiiiJjjjKkkk;

        private int mmmmNnnnOooo;

        public sbyte EeeeFfffGggg() {
            return this.eeeeFfffGggg;
        }

        public short IiiiJjjjKkkk() {
            return this.iiiiJjjjKkkk;
        }

        public int MmmmNnnnOooo() {
            return this.mmmmNnnnOooo;
        }

        public AaaaBbbbCcccDtoBuilder(sbyte eeeeFfffGggg, short iiiiJjjjKkkk, int mmmmNnnnOooo) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public AaaaBbbbCcccDtoBuilder(sbyte eeeeFfffGggg=1, short iiiiJjjjKkkk=2, int mmmmNnnnOooo=3) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public AaaaBbbbCcccDtoBuilder(AaaaBbbbCcccDto that) {
            this.eeeeFfffGggg = that.EeeeFfffGggg;
            this.iiiiJjjjKkkk = that.IiiiJjjjKkkk;
            this.mmmmNnnnOooo = that.MmmmNnnnOooo;
        }

        public AaaaBbbbCcccDto Build() {
        }

    }

}

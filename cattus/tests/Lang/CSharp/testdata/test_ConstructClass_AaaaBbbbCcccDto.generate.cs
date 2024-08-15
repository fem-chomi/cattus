namespace AaaaBbbbCccc {

    public class AaaaBbbbCcccDto {

        private readonly sbyte eeeeFfffGggg;

        private readonly short iiiiJjjjKkkk;

        private readonly int mmmmNnnnOooo;

        public sbyte EeeeFfffGggg() {
            return this.eeeeFfffGggg;
        }

        public short IiiiJjjjKkkk() {
            return this.iiiiJjjjKkkk;
        }

        public int MmmmNnnnOooo() {
            return this.mmmmNnnnOooo;
        }

        public AaaaBbbbCcccDto(sbyte eeeeFfffGggg, short iiiiJjjjKkkk, int mmmmNnnnOooo) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public AaaaBbbbCcccDto(sbyte eeeeFfffGggg=1, short iiiiJjjjKkkk=2, int mmmmNnnnOooo=3) {
            this.eeeeFfffGggg = eeeeFfffGggg;
            this.iiiiJjjjKkkk = iiiiJjjjKkkk;
            this.mmmmNnnnOooo = mmmmNnnnOooo;
        }

        public override string ToString() {
            return new StringBuilder()
                .Append($"EeeeFfffGggg: {this.EeeeFfffGggg}")
                .Append($"IiiiJjjjKkkk: {this.IiiiJjjjKkkk}")
                .Append($"MmmmNnnnOooo: {this.MmmmNnnnOooo}")
                .ToString();
        }

        public bool Equal() {
        }

        public int CompareTo() {
        }

        public string GetHashCode() {
        }

        public void ExportFile(string filename) {
        }

        public AaaaBbbbCcccDto ImportFile(string filename) {
        }

    }

}

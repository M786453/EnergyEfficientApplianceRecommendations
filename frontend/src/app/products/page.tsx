import { Box, Grid, Image, Text, Badge, VStack } from '@chakra-ui/react';

interface Product {
  id: number;
  name: string;
  description: string;
  image: string;
  price: number;
  availability: boolean;
  power: string;
  voltage: string;
}

const dummyProducts: Product[] = [
  {
    id: 1,
    name: 'Smart Refrigerator',
    description: 'Energy-efficient smart fridge with touchscreen',
    image: 'https://example.com/fridge.jpg',
    price: 1299.99,
    availability: true,
    power: '150W',
    voltage: '110V',
  },
  // Add more dummy products here
];

export default function Products() {
  return (
    <Box maxWidth="1200px" margin="auto" mt={8}>
      <Grid templateColumns="repeat(auto-fill, minmax(250px, 1fr))" gap={6}>
        {dummyProducts.map((product) => (
          <Box key={product.id} borderWidth="1px" borderRadius="lg" overflow="hidden">
            <Image src={product.image} alt={product.name} />
            <Box p="6">
              <VStack align="start" spacing={2}>
                <Text fontWeight="bold" fontSize="xl">
                  {product.name}
                </Text>
                <Text>{product.description}</Text>
                <Text fontWeight="bold" color="blue.500">
                  ${product.price.toFixed(2)}
                </Text>
                <Badge colorScheme={product.availability ? 'green' : 'red'}>
                  {product.availability ? 'In Stock' : 'Out of Stock'}
                </Badge>
                <Text>Power: {product.power}</Text>
                <Text>Voltage: {product.voltage}</Text>
              </VStack>
            </Box>
          </Box>
        ))}
      </Grid>
    </Box>
  );
}